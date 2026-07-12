#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Resvg } from "@resvg/resvg-js";
import { PNG } from "pngjs";
import gifenc from "gifenc";

const { GIFEncoder, quantize, applyPalette } = gifenc;
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "../..");

const previewTargets = [
  ["assets/hero/yash-kanadhia-alientech-motion.svg", "assets/hero/yash-kanadhia-alientech-preview.gif", 1600, 900, 14],
  ["assets/tooling/alientech-tool-constellation-motion.svg", "assets/tooling/alientech-tool-constellation-preview.gif", 1600, 640, 10],
  ["assets/motion/zeref-system-flow-motion.svg", "assets/motion/zeref-system-flow-preview.gif", 1600, 680, 14],
  ["assets/motion/product-working-model-motion.svg", "assets/motion/product-working-model-preview.gif", 1600, 520, 12],
];

const captures = [
  ["assets/hero/yash-kanadhia-alientech-motion.svg", 1600],
  ["assets/hero/yash-kanadhia-alientech-motion.svg", 1200],
  ["assets/hero/yash-kanadhia-alientech-motion.svg", 768],
  ["assets/hero/yash-kanadhia-alientech-motion.svg", 390],
  ["assets/tooling/alientech-tool-constellation-motion.svg", 1600],
  ["assets/tooling/alientech-tool-constellation-motion.svg", 1200],
  ["assets/tooling/alientech-tool-constellation-motion.svg", 768],
  ["assets/tooling/alientech-tool-constellation-motion.svg", 390],
  ["assets/motion/zeref-system-flow-motion.svg", 1600],
  ["assets/motion/zeref-system-flow-motion.svg", 1200],
  ["assets/motion/zeref-system-flow-motion.svg", 768],
  ["assets/motion/zeref-system-flow-motion.svg", 390],
  ["assets/motion/product-working-model-motion.svg", 1600],
  ["assets/motion/product-working-model-motion.svg", 1200],
  ["assets/motion/product-working-model-motion.svg", 768],
  ["assets/motion/product-working-model-motion.svg", 390],
];

function abs(file) {
  return path.join(root, file);
}

function ensure(file) {
  fs.mkdirSync(path.dirname(abs(file)), { recursive: true });
}

function overlayFor(svgPath, i, frames, width, height) {
  const t = i / frames;
  let x = width * (.12 + .76 * t);
  let y = height * .55;
  if (svgPath.includes("hero/")) y = height * (.72 - .32 * Math.sin(t * Math.PI));
  if (svgPath.includes("tool-constellation")) y = height * (.32 + .16 * Math.sin(t * Math.PI * 3));
  if (svgPath.includes("zeref-system-flow")) {
    x = width * (.44 + .12 * Math.sin(t * Math.PI * 4));
    y = height * (.17 + .68 * t);
  }
  if (svgPath.includes("product-working-model")) y = height * (.44 + .14 * Math.sin(t * Math.PI));
  return `<g id="preview-frame-signal" opacity=".86"><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="12" fill="#53E786" stroke="#06110B" stroke-width="3"/><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="28" fill="none" stroke="#53E786" stroke-width="3" opacity=".28"/></g>`;
}

function renderSvg(svgText, outFile, width) {
  ensure(outFile);
  const renderer = new Resvg(svgText, {
    fitTo: { mode: "width", value: width },
    font: {
      fontFiles: [],
      loadSystemFonts: true,
      defaultFontFamily: "Arial",
    },
  });
  fs.writeFileSync(abs(outFile), renderer.render().asPng());
}

function readPng(file) {
  return PNG.sync.read(fs.readFileSync(file));
}

function makeGif(frameFiles, width, height, outFile, delay) {
  const encoder = GIFEncoder();
  for (const file of frameFiles) {
    const png = readPng(file);
    const pixels = new Uint8Array(width * height * 4);
    for (let i = 0; i < pixels.length; i++) pixels[i] = png.data[i];
    const palette = quantize(pixels, 256);
    const indexed = applyPalette(pixels, palette);
    encoder.writeFrame(indexed, width, height, { palette, delay });
  }
  encoder.finish();
  ensure(outFile);
  fs.writeFileSync(abs(outFile), encoder.bytes());
}

function renderGifs() {
  const tmp = path.join(root, ".tmp-profile-preview");
  fs.mkdirSync(tmp, { recursive: true });
  for (const [svgPath, gifPath, sourceWidth, sourceHeight, duration] of previewTargets) {
    const base = fs.readFileSync(abs(svgPath), "utf8");
    const width = 960;
    const height = Math.round(width * sourceHeight / sourceWidth);
    const frames = 12;
    const delay = Math.round((duration * 1000) / frames);
    const files = [];
    for (let i = 0; i < frames; i++) {
      const frameSvg = base.replace("</svg>", `${overlayFor(svgPath, i, frames, sourceWidth, sourceHeight)}</svg>`);
      const frameFile = path.join(tmp, `${path.basename(gifPath)}-${i}.png`);
      const rel = path.relative(root, frameFile);
      renderSvg(frameSvg, rel, width);
      files.push(frameFile);
    }
    makeGif(files, width, height, gifPath, delay);
    console.log(`wrote ${gifPath}`);
  }
  fs.rmSync(tmp, { recursive: true, force: true });
}

function renderCaptures() {
  for (const [svgPath, width] of captures) {
    const svgText = fs.readFileSync(abs(svgPath), "utf8");
    const out = `docs/visual-system/render-captures/${path.basename(svgPath, ".svg")}-${width}.png`;
    renderSvg(svgText, out, width);
    console.log(`wrote ${out}`);
  }
  renderSvg(fs.readFileSync(abs("assets/social/github-profile-og.svg"), "utf8"), "assets/social/github-profile-og.png", 1280);
  console.log("wrote assets/social/github-profile-og.png");
}

renderGifs();
renderCaptures();
