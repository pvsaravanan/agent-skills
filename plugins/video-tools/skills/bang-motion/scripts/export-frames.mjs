/* =========================================================
   Render the opener to a PNG sequence, frame by frame.

   Not a screen recording: this script SETS the timeline time, waits for the
   browser to finish painting, and only then captures. So no frame is
   dropped even if one frame takes 300 ms to render.

   Prerequisites:
     npm i puppeteer
     python -m http.server 5178      (in the project folder, another window)

   Usage:
     node tools/export-frames.mjs
     ffmpeg -framerate 60 -i frames/f%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 opener.mp4
   ========================================================= */

import puppeteer from 'puppeteer';
import { mkdir } from 'node:fs/promises';

const URL   = process.env.URL   || 'http://127.0.0.1:5178/index.html?clean=1';
const FPS   = Number(process.env.FPS   || 60);
const OUT   = process.env.OUT   || 'frames';
const SCALE = Number(process.env.SCALE || 1);   // 1 = 1920x1080, 0.5 = 960x540

await mkdir(OUT, { recursive: true });

const browser = await puppeteer.launch({
  headless: 'new',
  args: ['--enable-gpu', '--use-gl=angle', '--enable-webgl', '--ignore-gpu-blocklist'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: SCALE });
await page.goto(URL, { waitUntil: 'networkidle0' });

// wait until the modules have loaded and the timeline is attached
await page.waitForFunction('window.OPENER && window.OPENER.ready && (!window.OPENER.clipsReady || window.OPENER.clipsReady())', { timeout: 120000 });
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => { window.OPENER.tl.pause(0); });

const DURATION = await page.evaluate(() => window.OPENER.DURATION);
const total = Math.ceil(DURATION * FPS);
console.log(`${total} frames @ ${FPS} fps (${DURATION}s) -> ${OUT}/`);

for(let i = 0; i < total; i++){
  const t = i / FPS;

  // set the time, then let TWO rAFs pass: one for GSAP to write the styles,
  // another for the render loop to draw the frame with those new values.
  await page.evaluate(async (time) => {
    if (window.OPENER.seekFrame) await window.OPENER.seekFrame(time);   // video clips present: wait for their frame to be ready
    else (window.OPENER.seek||window.OPENER.tl.time.bind(window.OPENER.tl))(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }, t);

  await page.screenshot({
    path: `${OUT}/f${String(i).padStart(5, '0')}.png`,
    clip: { x: 0, y: 0, width: 1920, height: 1080 },
    optimizeForSpeed: true,
  });

  if(i % FPS === 0) process.stdout.write(`\r${i}/${total}  ${t.toFixed(1)}s`);
}

console.log(`\ndone — ${total} frames in ${OUT}/`);
await browser.close();
