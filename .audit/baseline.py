#!/usr/bin/env python3
"""
Baseline health checks for joinery-site.
Checks: links, images, voice violations, SEO metadata.
"""

import json
import os
import re
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent.parent
TODAY = date.today().isoformat()
MANIFEST_PATH = ROOT / f".audit/screenshots/{TODAY}/manifest.json"
BASELINE_PATH = ROOT / f".audit/baseline/{TODAY}.json"

BANNED_WORDS = [
    "paradigm", "leverage", "passionate", "innovative",
    "synergy", "empower", "journey", "transformative"
]
BANNED_PHRASES = ["does the thinking", "holds itself", "zero-willpower"]

# Pages to check (all published HTML except dev/tools/copyright)
PAGES_TO_CHECK = [
    "index.html",
    "courses.html",
    "research.html",
    "about.html",
    "essays/the-wrong-question.html",
    "courses/foundations.html",
    "courses/brand-designer-track.html",
    "courses/copywriter-track.html",
    "courses/fiction-writer-track.html",
    "courses/nonfiction-writer-track.html",
    "courses/author-track.html",
    "courses/creative-director-track.html",
    "courses/educator-track.html",
    "courses/input-inversion.html",
    "courses/lens-extraction.html",
    "courses/voice-governance.html",
    "courses/semantic-hierarchy.html",
    "courses/coordinator-building.html",
]


class LinkImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.title = None
        self.description = None
        self.canonical = None
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img" and "src" in attrs:
            self.images.append(attrs["src"])
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            name = attrs.get("name", "").lower()
            prop = attrs.get("property", "").lower()
            content = attrs.get("content", "")
            if name == "description" or prop == "og:description":
                if not self.description:
                    self.description = content
            if attrs.get("rel") == "canonical" or tag == "link":
                pass
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title = data.strip()


def check_links_and_images(pages):
    link_failures = []
    image_failures = []

    for page_rel in pages:
        page_path = ROOT / page_rel
        if not page_path.exists():
            continue

        content = page_path.read_text(encoding="utf-8")
        parser = LinkImageParser()
        parser.feed(content)
        page_dir = page_path.parent

        for href in parser.links:
            # Skip external, anchor-only, mailto, javascript
            if href.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
                continue
            # Strip fragment
            href_clean = href.split("#")[0]
            if not href_clean:
                continue
            # Resolve relative to page dir
            if href_clean.startswith("/"):
                target = ROOT / href_clean.lstrip("/")
            else:
                target = (page_dir / href_clean).resolve()

            # Check if target exists (try as-is, and as dir/index.html)
            if not target.exists():
                if not (target / "index.html").exists():
                    link_failures.append({
                        "file": page_rel,
                        "target": href,
                        "reason": "file not found"
                    })

        for src in parser.images:
            if src.startswith(("http://", "https://", "data:")):
                continue
            if src.startswith("/"):
                target = ROOT / src.lstrip("/")
            else:
                target = (page_dir / src).resolve()
            if not target.exists():
                image_failures.append({
                    "file": page_rel,
                    "src": src,
                    "reason": "file not found"
                })

    return link_failures, image_failures


def check_voice(pages):
    failures = []

    for page_rel in pages:
        page_path = ROOT / page_rel
        if not page_path.exists():
            continue

        content = page_path.read_text(encoding="utf-8")
        # Strip HTML tags for text analysis
        text = re.sub(r"<[^>]+>", " ", content)
        lines = text.split("\n")

        for i, line in enumerate(lines, 1):
            line_lower = line.lower()

            # Em dashes
            if "\u2014" in line:
                # Ignore if inside a JSON-LD script block (won't catch everything but close enough)
                failures.append({
                    "file": page_rel, "line": i,
                    "type": "em-dash",
                    "text": line.strip()[:100]
                })

            # Banned words (whole word match)
            for word in BANNED_WORDS:
                if re.search(r"\b" + word + r"\b", line_lower):
                    failures.append({
                        "file": page_rel, "line": i,
                        "type": f"banned-word:{word}",
                        "text": line.strip()[:100]
                    })

            # Banned phrases
            for phrase in BANNED_PHRASES:
                if phrase in line_lower:
                    failures.append({
                        "file": page_rel, "line": i,
                        "type": f"banned-phrase",
                        "text": line.strip()[:100]
                    })

            # Negation-affirmation: "Not X. Y."
            if re.search(r"\bNot\s+\w.*?\.\s+[A-Z]", line):
                failures.append({
                    "file": page_rel, "line": i,
                    "type": "negation-affirmation",
                    "text": line.strip()[:100]
                })

    return failures


def check_seo(pages):
    failures = []

    for page_rel in pages:
        page_path = ROOT / page_rel
        if not page_path.exists():
            continue

        content = page_path.read_text(encoding="utf-8")
        parser = LinkImageParser()
        parser.feed(content)

        if not parser.title:
            failures.append({"file": page_rel, "missing": "title"})
        if not parser.description:
            failures.append({"file": page_rel, "missing": "meta description"})

    return failures


def run():
    print(f"Running baseline checks for {TODAY}...\n")

    link_failures, image_failures = check_links_and_images(PAGES_TO_CHECK)
    voice_failures = check_voice(PAGES_TO_CHECK)
    seo_failures = check_seo(PAGES_TO_CHECK)

    results = {
        "date": TODAY,
        "manifest": str(MANIFEST_PATH.relative_to(ROOT)),
        "checks": {
            "links":  {"pass": len(link_failures) == 0,  "failures": link_failures},
            "images": {"pass": len(image_failures) == 0, "failures": image_failures},
            "voice":  {"pass": len(voice_failures) == 0, "failures": voice_failures},
            "seo":    {"pass": len(seo_failures) == 0,   "failures": seo_failures},
        },
    }

    passed = sum(1 for c in results["checks"].values() if c["pass"])
    results["summary"] = f"{passed}/4 passed"

    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_PATH.write_text(json.dumps(results, indent=2))

    # Print report
    for check_name, check in results["checks"].items():
        status = "PASS" if check["pass"] else "FAIL"
        print(f"  {check_name.upper():<10} {status}")
        for f in check["failures"]:
            detail = f.get("target") or f.get("src") or f.get("missing") or f.get("type", "")
            text = f.get("text", "")
            print(f"             {f['file']} → {detail}")
            if text:
                print(f"             \"{text[:80]}\"")

    print(f"\n{results['summary']}. Baseline written to {BASELINE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    run()
