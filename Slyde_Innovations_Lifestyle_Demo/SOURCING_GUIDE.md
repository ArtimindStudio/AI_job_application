# Slyde Innovations — Curated Search & Sourcing Guide
## Manual Reference Acquisition for Premium / Copyrighted Databases

> **Purpose**: This guide provides optimized search queries and filtering
> strategies for sourcing high-signal reference imagery from databases that
> require manual browsing (no API scraping). Use alongside the automated
> `fetch_references.py` pipeline which covers Unsplash + Pexels.

---

## General Rules

- **NO CGI, 3D renders, or AI-generated imagery** — real photography only
- **Landscape orientation preferred** (16:9 or 3:2)
- **Minimum resolution**: 2400px on the long edge
- **Save files with prefix**: `manual_[category]_[##]_[source].jpg`
- **Drop files into** the matching `Ref_A/B/C` folder

---

## Category A — Product Identity (CMF)

### Target Subjects
Minimalist desk accessories, modular under-desk cable organizers, tech
hardware peripherals, docking stations, monitor arms, and premium desk
storage systems.

### CMF Criteria
| Attribute | Target |
|-----------|--------|
| Colors | Matte gray (#36454F), matte black (#28282B), anodized silver |
| Materials | Polycarbonate shells, powder-coated steel frames, anodized aluminum extrusions |
| Finishes | Matte, brushed metal, satin, powder-coat |
| Form | Clean linear edges, geometric, modular snap-fit |

### Search Queries by Platform

**ArchDaily** (archdaily.com)
- `minimalist office furniture product design`
- `desk accessories industrial design`
- `modular office system`
- Filter: Projects → Interior Design → Office

**Behance** (behance.net)
- `desk accessory product photography`
- `industrial design CMF matte black`
- `modular organizer product design`
- `tech accessory product photography`
- Filter: Industrial Design, Product Design, Photography

**Core77** (core77.com)
- `desk organizer design`
- `product design matte aluminum`
- `office accessories industrial design`
- Browse: Design Awards → Office / Workspace category

**Dezeen** (dezeen.com)
- `minimal desk accessories`
- `office product design`
- `modular desk system`

---

## Category B — Lighting & Environment

### Target Subjects
High-end corporate offices, modern co-working spaces, creative studios,
and architectural workspace interiors. Focus on **how light enters and
fills the space**.

### Lighting Criteria
| Attribute | Target |
|-----------|--------|
| Primary source | 45° directional window daylight |
| Shadow type | Linear, hard-edged cast shadows |
| Color temp | 5000K–6500K (neutral daylight) |
| Spatial palette | Cool grays, whites, muted light wood |
| Avoid | Warm tungsten, colored accent lighting, dark moody setups |

### Search Queries by Platform

**ArchDaily** (archdaily.com)
- `office interior natural light`
- `coworking space daylight design`
- `corporate office white interior architecture`
- `workspace natural lighting floor to ceiling windows`
- Filter: Projects → Office → sort by most recent

**Office Snapshots** (officesnapshots.com)
- `minimalist office`
- `natural light workspace`
- `white office interior`
- Browse: Featured Offices → filter by style: Minimal / Scandinavian

**Dezeen** (dezeen.com)
- `office interior natural daylight`
- `white workspace architecture`
- `minimal office design`

**Behance** (behance.net)
- `office interior photography natural light`
- `architectural workspace daylight`
- `modern office photography`
- Filter: Architecture, Interior Design, Photography

---

## Category C — Lifestyle & Scale

### Target Subjects
Creative professionals (designers, developers, strategists) naturally
interacting with desk setups. The human subject provides **scale reference**
for the product shots.

### Subject Criteria
| Attribute | Target |
|-----------|--------|
| Attire | Corporate-casual (no suits, no gym wear) |
| Interaction | Natural/candid — typing, sketching, reviewing screens |
| Lighting match | Ambient daylight on subject MUST match environmental light |
| Environment | Same office/workspace environments as Category B |
| Avoid | Staged/posed studio shots, greenscreen composites, stock-photo smiles |

### Search Queries by Platform

**Behance** (behance.net)
- `workspace lifestyle photography`
- `creative professional office candid`
- `corporate lifestyle photography natural light`
- `designer at desk photography`
- Filter: Photography → Editorial, Lifestyle

**Office Snapshots** (officesnapshots.com)
- Browse office tours — many include candid staff photos
- `people working office natural light`

**ArchDaily** (archdaily.com)
- Office project pages often include occupant photography
- `office interior people working`

**Getty Images** (gettyimages.com) — for reference only, licensing required
- `creative professional desk natural light editorial`
- `designer working modern office candid`
- Filter: Photography only, exclude illustrations

---

## Pro Tips for High-Signal Sourcing

1. **Reverse image search**: Once you find one strong reference, use
   Google Lens to find similar real-world photography.

2. **Photographer portfolios**: When you find a strong shot on Behance or
   ArchDaily, check the credited photographer's full portfolio.

3. **Architecture firm websites**: Firms like Gensler, Perkins&Will, and
   NBBJ publish high-res workspace photography in their project pages.

4. **Pinterest boards**: Search `"minimalist desk setup real photo"` and
   trace pins back to their original high-res sources.

5. **Filtering out CGI**: Look for these real-photo tells:
   - Sensor noise in shadow areas
   - Chromatic aberration at high-contrast edges
   - Imperfect reflections and micro-dust
   - Natural depth-of-field falloff
   - EXIF data (camera model, lens, ISO)

---

## Post-Download Checklist

- [ ] All files are ≥ 2400px on long edge
- [ ] No CGI / 3D renders / AI-generated images in the set
- [ ] Files follow naming convention: `manual_[category]_[##]_[source].jpg`
- [ ] Files are in the correct `Ref_A/B/C` folder
- [ ] Run `fetch_references.py` with `--verify` to regenerate metadata
- [ ] Review `reference_metadata.json` for completeness
