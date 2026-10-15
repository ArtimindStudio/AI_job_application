"""Weekly remote/AI job scan across public boards. Prints new candidates not yet in Airtable.

Usage: python scripts/weekly_remote_scan.py [days]   -> writes scripts/weekly_scan_hits.json
"""
import datetime as dt
import html
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "weekly_scan_hits.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 8
CUT = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=DAYS)

TITLE_KW = (r"(ai (trainer|training|tutor|evaluat|annotat|rater|content|creative|video|image|artist|generalist|writer|"
            r"specialist|data|task|response)|prompt|annotat|rlhf|data label|labell?ing|evaluator|rater|generative|genai|"
            r"gen ai|creative producer|motion design|video editor|content creator|e-?commerce|shopify|n8n|automation|ugc|"
            r"midjourney|ad creative|graphic design|visual design|email design|data analyst|product data|search quality|"
            r"vietnamese|data collection|audio recording|transcri)")
BAD = (r"(senior (backend|software|staff)|staff |principal|director|head of|vp |machine learning engineer|ml engineer|"
       r"devops|sre|security|account executive|sales|nurse|attorney|accountant|recruiter|kubernetes|kernel|chinese|"
       r"mandarin|japanese|korean|\bnsfw\b)")
GEO_BAD = (r"(us only|usa only|united states only|us-based|u\.s\. only|must be located in the (us|uk|eu)|canada only|"
           r"uk only|europe only|eu only|latam only|philippines-based)")
GEO_OK = r"(worldwide|anywhere|vietnam|asia|apac|global|^$|^remote$)"

# Local runs read .env; cloud runs get IDs from env vars and the token injected by the network proxy.
ENV_FILE = ROOT / ".env"
if ENV_FILE.exists():
    for line in ENV_FILE.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", " ", s or ""))).strip()


jobs = []


def add(src, title, company, url, date, loc, desc, salary=""):
    jobs.append(dict(source=src, title=clean(title), company=clean(company), url=url,
                     date=date.isoformat()[:10] if date else "", location=clean(loc),
                     desc=clean(desc)[:4000], salary=salary or ""))


def remoteok():
    for j in requests.get("https://remoteok.com/api", headers=UA, timeout=30).json()[1:]:
        d = dt.datetime.fromtimestamp(int(j.get("epoch", 0)), dt.timezone.utc)
        if d >= CUT:
            add("RemoteOK", j.get("position"), j.get("company"), j.get("url"), d, j.get("location", ""),
                j.get("description"), f'{j.get("salary_min", "")}-{j.get("salary_max", "")}')


def remotive():
    for j in requests.get("https://remotive.com/api/remote-jobs", headers=UA, timeout=60).json()["jobs"]:
        d = dt.datetime.fromisoformat(j["publication_date"]).replace(tzinfo=dt.timezone.utc)
        if d >= CUT:
            add("Remotive", j["title"], j["company_name"], j["url"], d, j.get("candidate_required_location", ""),
                j.get("description"), j.get("salary", ""))


def wwr():
    root = ET.fromstring(requests.get("https://weworkremotely.com/remote-jobs.rss", headers=UA, timeout=30).content)
    for it in root.iter("item"):
        d = parsedate_to_datetime(it.findtext("pubDate"))
        if d >= CUT:
            t = it.findtext("title") or ""
            comp, _, ttl = t.partition(": ")
            add("We Work Remotely", ttl or t, comp, it.findtext("link"), d, it.findtext("region") or "",
                it.findtext("description"))


def working_nomads():
    for j in requests.get("https://www.workingnomads.com/api/exposed_jobs/", headers=UA, timeout=30).json():
        d = dt.datetime.fromisoformat(j["pub_date"].replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        if d >= CUT:
            add("Working Nomads", j["title"], j.get("company_name", ""), j["url"], d, j.get("location", ""),
                j.get("description"))


def himalayas():
    for q in ["AI trainer", "prompt", "annotation", "AI evaluator", "AI video", "AI content", "Vietnamese",
              "data labeling", "ecommerce", "n8n", "creative", "designer"]:
        r = requests.get("https://himalayas.app/jobs/api/search", params={"q": q, "sort": "recent"},
                         headers=UA, timeout=30).json()
        for j in r.get("jobs", []):
            d = dt.datetime.fromtimestamp(int(j["pubDate"]), dt.timezone.utc)
            if d >= CUT:
                add("Himalayas", j["title"], j.get("companyName", ""), j.get("applicationLink") or j.get("guid"), d,
                    ", ".join(j.get("locationRestrictions") or []) or "Worldwide",
                    j.get("description") or j.get("excerpt"), f'{j.get("minSalary")}-{j.get("maxSalary")}')


def jobicy():
    for j in requests.get("https://jobicy.com/api/v2/remote-jobs?count=100", headers=UA, timeout=30).json().get("jobs", []):
        d = dt.datetime.fromisoformat(j["pubDate"].replace(" ", "T")).replace(tzinfo=dt.timezone.utc)
        if d >= CUT:
            add("Jobicy", j["jobTitle"], j["companyName"], j["url"], d, j.get("jobGeo", ""), j.get("jobDescription"))


RR_TITLES = ["AI Trainer", "Data Annotator", "AI Content Creator", "Prompt Engineer", "Video Editor",
             "Graphic Designer", "Content Creator", "AI Specialist", "Automation Specialist",
             "Ecommerce Specialist", "Data Analyst", "Transcriptionist"]


def remote_rocketship(max_pages=3):
    """Reads the server-rendered job list; `url` is the employer's own application page."""
    for title in RR_TITLES:
        for page in range(1, max_pages + 1):
            r = requests.get("https://www.remoterocketship.com/", headers=UA, timeout=40,
                             params={"page": page, "sort": "DateAdded", "locations": "Vietnam", "jobTitle": title})
            m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', r.text, re.S)
            rows = json.loads(m.group(1))["props"]["pageProps"].get("initialJobOpenings", []) if m else []
            if not rows:
                break
            fresh = 0
            for j in rows:
                d = dt.datetime.fromisoformat(j["created_at"])
                if d < CUT:
                    continue
                fresh += 1
                sal = (j.get("salaryRange") or {}).get("salaryHumanReadableText", "")
                add("Remote Rocketship", j["roleTitle"], (j.get("company") or {}).get("name", ""), j.get("url"), d,
                    j.get("location") or "", j.get("jobDescriptionSummary") or j.get("twoLineJobDescriptionSummary"), sal)
            if not fresh:
                break
            time.sleep(1)


def airtable_existing():
    pat = os.environ.get("AIRTABLE_PAT")
    h = {"Authorization": f"Bearer {pat}"} if pat else {}  # no PAT: the cloud proxy injects it
    url = f"https://api.airtable.com/v0/{os.environ['AIRTABLE_BASE_ID']}/{os.environ['AIRTABLE_TABLE_ID']}"
    titles, urls, off = set(), set(), None
    while True:
        p = {"fields[]": ["Title", "Job URL"]}
        if off:
            p["offset"] = off
        r = requests.get(url, headers=h, params=p, timeout=30)
        r.raise_for_status()
        r = r.json()
        for x in r["records"]:
            titles.add(x["fields"].get("Title", "").lower())
            urls.add(x["fields"].get("Job URL", ""))
        off = r.get("offset")
        if not off:
            return titles, urls


if __name__ == "__main__":
    for fn in (remoteok, remotive, wwr, working_nomads, himalayas, jobicy, remote_rocketship):
        n = len(jobs)
        try:
            fn()
        except Exception as e:
            print(f"{fn.__name__} failed: {e}")
        print(f"{fn.__name__}: {len(jobs) - n}")

    titles, urls = airtable_existing()
    seen, hits = set(), []
    for j in jobs:
        t = j["title"].lower()
        key = (t, j["company"].lower())
        if key in seen or t in titles or j["url"] in urls:
            continue
        seen.add(key)
        if not re.search(TITLE_KW, t) or re.search(BAD, t):
            continue
        blob = (j["location"] + " " + j["desc"][:1500]).lower()
        if re.search(GEO_BAD, blob) or not re.search(GEO_OK, j["location"].lower().strip()):
            continue
        hits.append(j)

    OUT.write_text(json.dumps(hits, indent=1), encoding="utf-8")
    print(f"\n{len(jobs)} fetched, {len(hits)} new candidates -> {OUT.name}")
    for i, j in enumerate(hits):
        print(i, "|", j["source"], "|", j["date"], "|", j["title"][:60], "|", j["company"][:24], "|",
              j["location"][:22], "|", j["salary"][:28])
