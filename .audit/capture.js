#!/usr/bin/env node
/**
 * Playwright capture for joinery-site audit.
 * Run from joinery-site root: node .audit/capture.js
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const BASE = 'http://localhost:4002';
const TODAY = new Date().toISOString().slice(0, 10);
const AUDIT_DIR = `.audit/screenshots/${TODAY}`;

const PAGES = [
  { slug: 'index',                    url: '/',                                         title: 'Homepage' },
  { slug: 'courses',                  url: '/courses.html',                             title: 'Curriculum' },
  { slug: 'foundations',              url: '/courses/foundations.html',                 title: 'Foundations' },
  { slug: 'brand-designer-track',     url: '/courses/brand-designer-track.html',        title: 'Brand Designer Track' },
  { slug: 'copywriter-track',         url: '/courses/copywriter-track.html',            title: 'Copywriter Track' },
  { slug: 'fiction-writer-track',     url: '/courses/fiction-writer-track.html',        title: 'Fiction Writer Track' },
  { slug: 'nonfiction-writer-track',  url: '/courses/nonfiction-writer-track.html',     title: 'Nonfiction Writer Track' },
  { slug: 'creative-director-track',  url: '/courses/creative-director-track.html',     title: 'Creative Director Track' },
  { slug: 'educator-track',           url: '/courses/educator-track.html',              title: 'Educator Track' },
  { slug: 'author-track',             url: '/courses/author-track.html',                title: 'Author Track' },
  { slug: 'research',                 url: '/research.html',                            title: 'Research' },
  { slug: 'about',                    url: '/about.html',                               title: 'About' },
  { slug: 'essay-the-wrong-question', url: '/essays/the-wrong-question.html',           title: 'Essay: The Wrong Question' },
];

const VIEWPORTS = {
  mobile:  { width: 375,  height: 812 },
  tablet:  { width: 768,  height: 1024 },
  desktop: { width: 1440, height: 900 },
};

async function capture() {
  // Ensure dirs exist
  for (const vp of Object.keys(VIEWPORTS)) {
    fs.mkdirSync(`${AUDIT_DIR}/${vp}`, { recursive: true });
  }

  const browser = await chromium.launch();
  const manifest = { date: TODAY, server: BASE, pages: [], total_pages: 0, total_screenshots: 0 };
  let shotCount = 0;

  for (const pageDef of PAGES) {
    const entry = { url: pageDef.url, title: pageDef.title, screenshots: {} };
    const url = BASE + pageDef.url;

    for (const [vpName, vpSize] of Object.entries(VIEWPORTS)) {
      const page = await browser.newPage({ viewport: vpSize });
      const outPath = `${AUDIT_DIR}/${vpName}/${pageDef.slug}.png`;
      try {
        await page.goto(url, { waitUntil: 'networkidle', timeout: 15000 });
        await page.screenshot({ path: outPath, fullPage: true });
        entry.screenshots[vpName] = outPath;
        shotCount++;
        process.stdout.write(`  ${vpName.padEnd(8)} ${pageDef.slug}\n`);
      } catch (e) {
        process.stdout.write(`  ERROR ${vpName} ${pageDef.slug}: ${e.message}\n`);
        entry.screenshots[vpName] = null;
      } finally {
        await page.close();
      }
    }

    manifest.pages.push(entry);
  }

  await browser.close();

  manifest.total_pages = manifest.pages.length;
  manifest.total_screenshots = shotCount;

  const manifestPath = `.audit/screenshots/${TODAY}/manifest.json`;
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));

  console.log(`\nCaptured ${manifest.total_pages} pages x 3 viewports = ${shotCount} screenshots.`);
  console.log(`Manifest: ${manifestPath}`);
}

capture().catch(e => { console.error(e); process.exit(1); });
