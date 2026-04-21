#!/usr/bin/env python3
"""Playwright capture for joinery-site audit."""

import json
import os
from datetime import date
from playwright.sync_api import sync_playwright

BASE = "http://localhost:4002"
TODAY = date.today().isoformat()
AUDIT_DIR = f".audit/screenshots/{TODAY}"

PAGES = [
    {"slug": "index",                          "url": "/",                                          "title": "Homepage"},
    {"slug": "courses",                         "url": "/courses.html",                              "title": "Curriculum"},
    {"slug": "foundations",                     "url": "/courses/foundations.html",                  "title": "Foundations"},
    {"slug": "brand-designer-track",            "url": "/courses/brand-designer-track.html",         "title": "Brand Designer Track"},
    {"slug": "copywriter-track",                "url": "/courses/copywriter-track.html",             "title": "Copywriter Track"},
    {"slug": "fiction-writer-track",            "url": "/courses/fiction-writer-track.html",         "title": "Fiction Writer Track"},
    {"slug": "nonfiction-writer-track",         "url": "/courses/nonfiction-writer-track.html",      "title": "Nonfiction Writer Track"},
    {"slug": "creative-director-track",         "url": "/courses/creative-director-track.html",      "title": "Creative Director Track"},
    {"slug": "educator-track",                  "url": "/courses/educator-track.html",               "title": "Educator Track"},
    {"slug": "author-track",                    "url": "/courses/author-track.html",                 "title": "Author Track"},
    {"slug": "research",                        "url": "/research.html",                             "title": "Research"},
    {"slug": "about",                           "url": "/about.html",                                "title": "About"},
    {"slug": "essay-the-wrong-question",        "url": "/essays/the-wrong-question.html",            "title": "Essay: The Wrong Question"},
]

VIEWPORTS = {
    "mobile":  {"width": 375,  "height": 812},
    "tablet":  {"width": 768,  "height": 1024},
    "desktop": {"width": 1440, "height": 900},
}

def capture():
    manifest = {
        "date": TODAY,
        "server": BASE,
        "pages": [],
        "total_pages": 0,
        "total_screenshots": 0,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for page_def in PAGES:
            slug = page_def["slug"]
            url = BASE + page_def["url"]
            entry = {
                "url": page_def["url"],
                "title": page_def["title"],
                "screenshots": {}
            }

            for vp_name, vp_size in VIEWPORTS.items():
                page = browser.new_page(viewport=vp_size)
                try:
                    page.goto(url, wait_until="networkidle", timeout=10000)
                    path = f"{AUDIT_DIR}/{vp_name}/{slug}.png"
                    page.screenshot(path=path, full_page=True)
                    entry["screenshots"][vp_name] = path
                    print(f"  {vp_name:8} {slug}")
                except Exception as e:
                    print(f"  ERROR {vp_name} {slug}: {e}")
                    entry["screenshots"][vp_name] = None
                finally:
                    page.close()

            manifest["pages"].append(entry)

        browser.close()

    manifest["total_pages"] = len(manifest["pages"])
    manifest["total_screenshots"] = sum(
        1 for p in manifest["pages"]
        for s in p["screenshots"].values()
        if s is not None
    )

    manifest_path = f".audit/screenshots/{TODAY}/manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nCaptured {manifest['total_pages']} pages x 3 viewports = {manifest['total_screenshots']} screenshots.")
    print(f"Manifest written to {manifest_path}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    capture()
