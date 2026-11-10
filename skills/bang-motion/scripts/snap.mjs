/* =========================================================
   VISUAL VERIFICATION: snapshot a few key seconds, not a full render.

   An AI cannot watch video — it can only LOOK at frames. This script
   freezes the timeline at the requested seconds (OPENER.seek), waits for the
   browser to finish painting, then takes a screenshot. 6–20 frames are enough
   to judge one explainer; do NOT render every frame just to check
   (60 s × 60 fps = 3,600 images — that is export-frames.mjs's job, and only
   when the user asks for an MP4).

   Prerequisite (optional — without Node, verify manually via ?debug=1):
     npm i puppeteer            (once, in any folder; run from there)

   Usage (from the project folder, no server; the file is opened via file://):
     node <path>/snap.mjs shots 1 3.5 8 12 20
     URL="file:///C:/project/index.html?clean=1" node <path>/snap.mjs shots 1 3.5 8
   Output: shots/t1_00.png, shots/t3_50.png, ... — combine into a contact
   sheet (PIL/ffmpeg tile) and JUDGE with your eyes: text clipped? overlapping?
   text appearing before the camera finishes? still feels like a slide?

   The page must expose window.OPENER = { W, H, ready, seek(t) } — every
   starter in this skill already does. ?clean=1 holds autoplay & the panel.
   ========================================================= */
import puppeteer from 'puppeteer';
import { pathToFileURL } from 'node:url';
import { mkdir } from 'node:fs/promises';

const [outDir, ...times] = process.argv.slice(2);
if (!outDir || !times.length) { console.log('usage: node snap.mjs <output-folder> <seconds> [<seconds> ...]'); process.exit(1); }
const URL = process.env.URL || pathToFileURL(process.cwd()).href + '/index.html?clean=1';
await mkdir(outDir, { recursive: true });
const browser = await puppeteer.launch({ headless: 'new', args: ['--enable-gpu', '--use-gl=angle', '--enable-webgl', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'] });
const page = await browser.newPage();
page.on('pageerror', e => console.log('PAGEERROR', e.message));
await page.goto(URL, { waitUntil: 'networkidle0' });
await page.waitForFunction('window.OPENER && window.OPENER.ready && (!window.OPENER.clipsReady || window.OPENER.clipsReady())', { timeout: 60000 });
const { W, H } = await page.evaluate(() => ({ W: window.OPENER.W || 1920, H: window.OPENER.H || 1080 }));
await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
for (const ts of times) {
  const t = Number(ts);
  await page.evaluate(async (time) => {
    if (window.OPENER.seekFrame) { await window.OPENER.seekFrame(time); window.OPENER.seek(time); }   // video clips present
    else {
      window.OPENER.seek(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    window.OPENER.seek(time);   // twice: GSAP writes the style, then the render loop draws
    }
  }, t);
  await page.screenshot({ path: `${outDir}/t${t.toFixed(2).replace('.', '_')}.png`, clip: { x: 0, y: 0, width: W, height: H } });
  process.stdout.write(`${t} `);
}
await browser.close(); console.log('\ndone');
