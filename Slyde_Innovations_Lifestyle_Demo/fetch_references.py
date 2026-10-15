"""
Slyde Innovations Lifestyle Demo — Automated Reference Acquisition Script
==========================================================================
Downloads curated reference imagery from Unsplash and Pexels APIs into
the project's three reference buckets.

Requirements:
    pip install requests

Usage:
    1. Get free API keys:
       - Unsplash: https://unsplash.com/developers
       - Pexels:   https://www.pexels.com/api/
    2. Set them as environment variables (or paste them below):
       $env:UNSPLASH_ACCESS_KEY = "your_key_here"
       $env:PEXELS_API_KEY      = "your_key_here"
    3. Run:
       python fetch_references.py
"""

import os
import sys
import json
import time
import hashlib
import requests
from pathlib import Path
from datetime import datetime, timezone

# ─── Configuration ───────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent

FOLDERS = {
    "identity":  BASE_DIR / "Ref_A_Identity",
    "lighting":  BASE_DIR / "Ref_B_Lighting",
    "lifestyle": BASE_DIR / "Ref_C_Lifestyle",
}

IMAGES_PER_CATEGORY = 15

# API keys — set via env vars or hardcode here (not recommended for sharing)
UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")
PEXELS_KEY   = os.getenv("PEXELS_API_KEY", "")

# ─── Search Queries ──────────────────────────────────────────────────────────
# Each category has multiple queries to maximize coverage.
# Queries are intentionally specific to surface real-world photography.

SEARCH_QUERIES = {
    "identity": [
        "minimalist desk accessories matte black",
        "modular desk organizer aluminum",
        "tech hardware product photography",
        "polycarbonate desk accessory minimal",
        "powder coated steel desk setup",
        "anodized aluminum desk gadget",
        "clean desk accessories product photo",
        "modern desk organizer industrial design",
    ],
    "lighting": [
        "modern office natural window light",
        "architectural office interior daylight",
        "coworking space clean white interior",
        "minimal office directional sunlight shadows",
        "corporate office natural light neutral palette",
        "modern workspace window daylight",
        "clean office interior cool gray",
        "scandinavian office natural light",
    ],
    "lifestyle": [
        "creative professional desk setup natural light",
        "person working modern office daylight",
        "corporate casual desk workspace photography",
        "designer working at desk natural light",
        "professional using laptop modern office",
        "creative workspace lifestyle photography",
        "person at minimalist desk real photo",
        "office lifestyle candid work desk",
    ],
}

# ─── API Clients ─────────────────────────────────────────────────────────────

class UnsplashClient:
    """Thin wrapper around the Unsplash API."""

    BASE = "https://api.unsplash.com"

    def __init__(self, access_key: str):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Client-ID {access_key}"
        self.session.headers["Accept-Version"] = "v1"

    def search(self, query: str, per_page: int = 10, page: int = 1) -> list[dict]:
        """Return a list of photo dicts from Unsplash search."""
        resp = self.session.get(
            f"{self.BASE}/search/photos",
            params={
                "query": query,
                "per_page": per_page,
                "page": page,
                "orientation": "landscape",
                "content_filter": "high",
            },
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json().get("results", [])

    @staticmethod
    def extract(photo: dict) -> dict:
        """Normalize an Unsplash photo dict into our internal format."""
        return {
            "id": photo["id"],
            "source": "unsplash",
            "url_full": photo["urls"]["full"],
            "url_regular": photo["urls"]["regular"],
            "download_link": photo["links"]["download"],
            "width": photo["width"],
            "height": photo["height"],
            "description": photo.get("description") or photo.get("alt_description") or "",
            "photographer": photo["user"]["name"],
            "photographer_url": photo["user"]["links"]["html"],
            "license": "Unsplash License (free)",
        }


class PexelsClient:
    """Thin wrapper around the Pexels API."""

    BASE = "https://api.pexels.com/v1"

    def __init__(self, api_key: str):
        self.session = requests.Session()
        self.session.headers["Authorization"] = api_key

    def search(self, query: str, per_page: int = 10, page: int = 1) -> list[dict]:
        """Return a list of photo dicts from Pexels search."""
        resp = self.session.get(
            f"{self.BASE}/search",
            params={
                "query": query,
                "per_page": per_page,
                "page": page,
                "orientation": "landscape",
                "size": "large",
            },
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json().get("photos", [])

    @staticmethod
    def extract(photo: dict) -> dict:
        """Normalize a Pexels photo dict into our internal format."""
        return {
            "id": str(photo["id"]),
            "source": "pexels",
            "url_full": photo["src"]["original"],
            "url_regular": photo["src"]["large2x"],
            "download_link": photo["src"]["original"],
            "width": photo["width"],
            "height": photo["height"],
            "description": photo.get("alt") or "",
            "photographer": photo["photographer"],
            "photographer_url": photo.get("photographer_url", ""),
            "license": "Pexels License (free)",
        }


# ─── Download Engine ─────────────────────────────────────────────────────────

def download_image(url: str, dest: Path, source: str = "unsplash") -> dict | None:
    """Download a single image and return file metadata, or None on failure."""
    try:
        headers = {}
        if source == "unsplash" and UNSPLASH_KEY:
            headers["Authorization"] = f"Client-ID {UNSPLASH_KEY}"

        resp = requests.get(url, headers=headers, timeout=30, stream=True)
        resp.raise_for_status()

        content = resp.content
        md5 = hashlib.md5(content).hexdigest()
        sha256 = hashlib.sha256(content).hexdigest()

        dest.write_bytes(content)

        return {
            "file": dest.name,
            "path": str(dest),
            "size_bytes": len(content),
            "md5": md5,
            "sha256": sha256,
            "content_type": resp.headers.get("Content-Type", "unknown"),
        }
    except Exception as e:
        print(f"  ✗ Failed to download {url}: {e}")
        return None


def fetch_category(
    category: str,
    queries: list[str],
    unsplash: UnsplashClient | None,
    pexels: PexelsClient | None,
    limit: int = 15,
) -> list[dict]:
    """
    Fetch up to `limit` unique images for a category by cycling through
    queries across both APIs. Returns list of metadata dicts.
    """
    dest_dir = FOLDERS[category]
    dest_dir.mkdir(parents=True, exist_ok=True)

    seen_ids: set[str] = set()
    candidates: list[dict] = []

    # Gather candidates from both APIs
    for query in queries:
        if len(candidates) >= limit * 2:
            break  # we have more than enough candidates

        if unsplash:
            try:
                results = unsplash.search(query, per_page=8)
                for photo in results:
                    info = UnsplashClient.extract(photo)
                    if info["id"] not in seen_ids:
                        seen_ids.add(info["id"])
                        candidates.append(info)
                time.sleep(0.5)  # rate-limit courtesy
            except Exception as e:
                print(f"  ⚠ Unsplash query '{query}' failed: {e}")

        if pexels:
            try:
                results = pexels.search(query, per_page=8)
                for photo in results:
                    info = PexelsClient.extract(photo)
                    if info["id"] not in seen_ids:
                        seen_ids.add(info["id"])
                        candidates.append(info)
                time.sleep(0.3)
            except Exception as e:
                print(f"  ⚠ Pexels query '{query}' failed: {e}")

    # Sort by resolution (width * height) descending — prefer highest res
    candidates.sort(key=lambda c: c["width"] * c["height"], reverse=True)

    # Download top N
    downloaded: list[dict] = []
    for i, cand in enumerate(candidates):
        if len(downloaded) >= limit:
            break

        ext = "jpg"
        filename = f"{category}_{len(downloaded)+1:02d}_{cand['source']}_{cand['id']}.{ext}"
        dest_path = dest_dir / filename

        print(f"  ↓ [{len(downloaded)+1}/{limit}] {cand['source']}:{cand['id']} → {filename}")

        file_meta = download_image(cand["url_regular"], dest_path, cand["source"])
        if file_meta:
            downloaded.append({**cand, **file_meta})
            time.sleep(0.3)

    return downloaded


# ─── Metadata Generation ────────────────────────────────────────────────────

def generate_metadata(all_results: dict[str, list[dict]]) -> dict:
    """Build the JSON metadata summary for the entire dataset."""
    meta = {
        "project": "Slyde Innovations Lifestyle Demo",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline_version": "1.0.0",
        "categories": {},
        "cmf_analysis": {
            "dominant_materials": [
                "matte polycarbonate (black/gray)",
                "powder-coated steel",
                "anodized aluminum",
                "light wood veneer",
            ],
            "dominant_colors": [
                {"name": "charcoal", "hex": "#36454F"},
                {"name": "matte black", "hex": "#28282B"},
                {"name": "cool gray", "hex": "#8D99AE"},
                {"name": "warm white", "hex": "#FAF9F6"},
                {"name": "muted oak", "hex": "#C4A882"},
            ],
            "dominant_finishes": [
                "matte",
                "brushed metal",
                "satin",
                "powder-coat",
            ],
        },
        "lighting_analysis": {
            "primary_angle": "45° directional daylight (window-side)",
            "secondary_fill": "ambient ceiling bounce / reflected daylight",
            "shadow_type": "linear, hard-edged from single window source",
            "color_temperature_range": "5000K–6500K (neutral daylight)",
            "spatial_palette": ["cool grays", "whites", "muted light wood"],
        },
        "total_images": 0,
        "sources_used": [],
    }

    sources = set()
    total = 0

    for cat_key, images in all_results.items():
        cat_meta = {
            "count": len(images),
            "images": [],
        }
        for img in images:
            sources.add(img["source"])
            cat_meta["images"].append({
                "file": img.get("file", ""),
                "source": img["source"],
                "photographer": img["photographer"],
                "photographer_url": img["photographer_url"],
                "license": img["license"],
                "resolution": f"{img['width']}x{img['height']}",
                "description": img["description"],
                "md5": img.get("md5", ""),
                "sha256": img.get("sha256", ""),
                "size_bytes": img.get("size_bytes", 0),
            })
        total += len(images)
        meta["categories"][cat_key] = cat_meta

    meta["total_images"] = total
    meta["sources_used"] = sorted(sources)

    return meta


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print("=" * 68)
    print("  Slyde Innovations — Reference Acquisition Pipeline v1.0")
    print("=" * 68)

    # Validate API keys
    if not UNSPLASH_KEY and not PEXELS_KEY:
        print("\n✗ ERROR: No API keys found.")
        print("  Set at least one of these environment variables:")
        print("    $env:UNSPLASH_ACCESS_KEY = 'your_key'")
        print("    $env:PEXELS_API_KEY      = 'your_key'")
        print("\n  Get free keys at:")
        print("    → https://unsplash.com/developers")
        print("    → https://www.pexels.com/api/")
        sys.exit(1)

    unsplash = UnsplashClient(UNSPLASH_KEY) if UNSPLASH_KEY else None
    pexels   = PexelsClient(PEXELS_KEY) if PEXELS_KEY else None

    active_sources = []
    if unsplash:
        active_sources.append("Unsplash")
    if pexels:
        active_sources.append("Pexels")
    print(f"\n✓ Active sources: {', '.join(active_sources)}")
    print(f"✓ Target: {IMAGES_PER_CATEGORY} images × 3 categories = {IMAGES_PER_CATEGORY * 3} total")
    print(f"✓ Base directory: {BASE_DIR}\n")

    all_results: dict[str, list[dict]] = {}

    for category, queries in SEARCH_QUERIES.items():
        label = {
            "identity":  "Ref_A_Identity  (Product / CMF)",
            "lighting":  "Ref_B_Lighting  (Environment / Light)",
            "lifestyle": "Ref_C_Lifestyle (Lifestyle / Scale)",
        }[category]

        print(f"─── {label} {'─' * (50 - len(label))}")
        results = fetch_category(category, queries, unsplash, pexels, IMAGES_PER_CATEGORY)
        all_results[category] = results
        print(f"  ✓ Downloaded {len(results)}/{IMAGES_PER_CATEGORY}\n")

    # Generate and save metadata
    print("─── Generating Metadata ─────────────────────────────────────")
    metadata = generate_metadata(all_results)
    meta_path = BASE_DIR / "reference_metadata.json"
    meta_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  ✓ Metadata written to {meta_path}")

    # Integrity report
    print("\n─── Integrity Report ────────────────────────────────────────")
    for cat_key, images in all_results.items():
        folder = FOLDERS[cat_key]
        print(f"  {folder.name}: {len(images)} files")
        for img in images:
            status = "✓" if img.get("size_bytes", 0) > 0 else "✗"
            print(f"    {status} {img.get('file', '?')} ({img.get('size_bytes', 0):,} bytes) [{img.get('md5', '?')[:8]}]")

    total = sum(len(v) for v in all_results.values())
    print(f"\n{'=' * 68}")
    print(f"  ✓ Pipeline complete. {total}/{IMAGES_PER_CATEGORY * 3} references acquired.")
    print(f"  ✓ Workspace ready for Google Flow / Nano Banana Tools style-injection.")
    print(f"{'=' * 68}")


if __name__ == "__main__":
    main()
