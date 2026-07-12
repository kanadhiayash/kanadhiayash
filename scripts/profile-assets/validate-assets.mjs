#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "../..");

const required = [
  "assets/hero/yash-kanadhia-alientech-motion.svg",
  "assets/hero/yash-kanadhia-alientech-static.svg",
  "assets/hero/yash-kanadhia-alientech-preview.gif",
  "assets/tooling/alientech-tool-constellation-motion.svg",
  "assets/tooling/alientech-tool-constellation-static.svg",
  "assets/tooling/alientech-tool-constellation-preview.gif",
  "assets/motion/zeref-system-flow-motion.svg",
  "assets/motion/zeref-system-flow-static.svg",
  "assets/motion/zeref-system-flow-preview.gif",
  "assets/motion/product-working-model-motion.svg",
  "assets/motion/product-working-model-static.svg",
  "assets/motion/product-working-model-preview.gif",
  "assets/social/github-profile-og.png",
  "docs/visual-system/logo-sources.md",
];

const logos = ["figma", "linear", "notion", "react", "swiftui", "firebase", "claude", "codex", "github"];
for (const logo of logos) required.push(`assets/tooling/logos/${logo}.svg`);
for (const badge of ["verified", "documented", "team-project", "independent", "prototype", "simulated", "known-boundary", "media-parked"]) required.push(`assets/ui/badges/${badge}.svg`);
for (const section of ["overview", "selected-work", "capabilities", "evidence", "how-i-work", "stack", "current-signals", "connect"]) required.push(`assets/ui/sections/${section}.svg`);
for (const portal of ["zeref", "perfin", "for-rent", "streamnexus"]) required.push(`assets/project-portals/${portal}-media-parked.svg`);

const animated = required.filter((file) => file.endsWith("-motion.svg"));
const forbidden = [/<script/i, /javascript:/i, /<foreignObject/i, /\sonload=/i, /\sonclick=/i, /url\(\s*["']?https?:/i, /xlink:href=["'](?!#)/i, /\bhref=["'](?!#)/i];
const outOfScopeMissing = new Set([
  "./assets/profile-media/zeref-product-proof.gif",
  "./assets/profile-media/perfin-os-product-proof.gif",
  "./assets/profile-media/for-rent-product-proof.gif",
  "./assets/profile-media/streamnexus-product-proof.gif",
]);

function rel(file) {
  return path.join(root, file);
}

function fail(errors, message) {
  errors.push(message);
}

function parseSvg(file, errors) {
  const text = fs.readFileSync(rel(file), "utf8");
  const rootMatch = text.match(/<svg\b([^>]*)>/i);
  if (!rootMatch) fail(errors, `${file} does not contain an SVG root`);
  const attrs = rootMatch?.[1] ?? "";
  if (!/\bviewBox=["'][^"']+["']/.test(attrs)) fail(errors, `${file} is missing viewBox`);
  if (!/\brole=["']img["']/.test(attrs)) fail(errors, `${file} is missing role="img"`);
  if (!/\baria-labelledby=["'][^"']+["']/.test(attrs)) fail(errors, `${file} is missing aria-labelledby`);
  if (!text.includes("<title") || !text.includes("<desc")) fail(errors, `${file} is missing title or desc`);
  for (const pattern of forbidden) {
    if (pattern.test(text)) fail(errors, `${file} contains forbidden SVG token ${pattern}`);
  }
  if (animated.includes(file) && !text.includes("prefers-reduced-motion")) fail(errors, `${file} is missing reduced-motion handling`);
}

function imageReferences(readme) {
  const refs = [];
  for (const match of readme.matchAll(/<img\b[^>]*\bsrc=["']([^"']+)["'][^>]*>/gi)) refs.push(match[1]);
  for (const match of readme.matchAll(/!\[[^\]]*]\(([^)\s]+)(?:\s+["'][^"']*["'])?\)/g)) refs.push(match[1]);
  return refs;
}

function checkReadmeAssets(errors) {
  const readme = fs.readFileSync(rel("README.md"), "utf8");
  for (const ref of imageReferences(readme)) {
    if (!ref.startsWith("./assets/")) continue;
    if (outOfScopeMissing.has(ref)) continue;
    const clean = ref.replace(/^\.\//, "");
    if (!fs.existsSync(rel(clean))) fail(errors, `README image path is broken: ${ref}`);
  }
  for (const ref of [
    "./assets/hero/yash-kanadhia-alientech-motion.svg",
    "./assets/hero/yash-kanadhia-alientech-static.svg",
    "./assets/motion/zeref-system-flow-motion.svg",
    "./assets/motion/product-working-model-motion.svg",
    "./assets/tooling/alientech-tool-constellation-motion.svg",
  ]) {
    if (!readme.includes(ref)) fail(errors, `README is missing in-scope asset reference ${ref}`);
  }
}

function checkLogoSources(errors) {
  const text = fs.readFileSync(rel("docs/visual-system/logo-sources.md"), "utf8");
  for (const logo of ["Figma", "Linear", "Notion", "React", "SwiftUI", "Firebase", "Claude", "Codex", "GitHub"]) {
    if (!text.includes(`| ${logo} |`)) fail(errors, `Logo source record missing for ${logo}`);
  }
}

function sha(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(rel(file))).digest("hex");
}

const errors = [];
for (const file of required) {
  if (!fs.existsSync(rel(file))) {
    fail(errors, `Missing required file: ${file}`);
    continue;
  }
  if (fs.statSync(rel(file)).size === 0) fail(errors, `Empty required file: ${file}`);
  if (file.endsWith(".svg")) parseSvg(file, errors);
}
checkReadmeAssets(errors);
checkLogoSources(errors);

console.log("Organic AlienTech asset validation");
if (errors.length) {
  console.log("Result: BLOCKED");
  for (const error of errors) console.log(`  ERROR: ${error}`);
  process.exit(1);
}
console.log("Result: PASS");
console.log(`  OK: ${required.length} required files exist.`);
console.log("  OK: SVG files parse, include viewBox, metadata, role, and safe references.");
console.log("  OK: Animated SVGs include reduced-motion handling.");
console.log("  OK: In-scope README asset paths resolve; parked project-evidence GIFs are excluded.");
console.log(`  OK: Hero motion sha256 ${sha("assets/hero/yash-kanadhia-alientech-motion.svg").slice(0, 12)}`);
