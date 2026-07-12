#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import * as icons from "simple-icons";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "../..");
const today = "2026-07-12";

const tokenCss = `
  :root{--mineral-bg:#F5F8F4;--mineral-surface:#E9F0EA;--mineral-line:#B9CCBE;--bio-void:#06110B;--bio-panel:#0A1A11;--bio-panel-2:#102419;--ink-primary:#13241A;--ink-secondary:#496255;--ink-on-dark:#EAF7EE;--signal-deep:#13743F;--signal:#53E786;--signal-soft:#95F5B4}
  .sans{font-family:Inter,Arial,system-ui,sans-serif}.mono{font-family:SFMono-Regular,Consolas,"Liberation Mono",monospace}.title{letter-spacing:.02em}.small{letter-spacing:.12em}.micro{letter-spacing:.16em}
  .panel{fill:#0A1A11;stroke:#B9CCBE;stroke-width:1.4}.shell{fill:#F5F8F4;stroke:#13743F;stroke-width:1.5}.label{fill:#13241A}.muted{fill:#496255}.darkText{fill:#EAF7EE}.signal{stroke:#53E786;fill:none;stroke-linecap:round;stroke-linejoin:round}.softSignal{stroke:#95F5B4;fill:none;stroke-linecap:round;stroke-linejoin:round}.line{stroke:#B9CCBE;fill:none;stroke-linecap:round}.node{fill:#95F5B4;stroke:#13743F;stroke-width:1.2}
`;

const motionCss = `
  .breathe{animation:breathe 8s cubic-bezier(.42,0,.2,1) infinite}.seed{animation:seed 10s cubic-bezier(.42,0,.2,1) infinite}.signalPath{stroke-dasharray:12 26;animation:dash 8s linear infinite}.signalPathSlow{stroke-dasharray:8 34;animation:dash 13s linear infinite}.irisA{transform-origin:center;animation:spinA 14s linear infinite}.irisB{transform-origin:center;animation:spinB 18s linear infinite}.wake{animation:wake 14s cubic-bezier(.42,0,.2,1) infinite}.stagePulse{animation:stagePulse 12s cubic-bezier(.42,0,.2,1) infinite}.toolPulse{animation:toolPulse 10s cubic-bezier(.42,0,.2,1) infinite}.trace{stroke-dasharray:0 700;animation:trace 14s cubic-bezier(.42,0,.2,1) infinite}
  @keyframes breathe{0%,100%{opacity:.82}50%{opacity:1}}@keyframes seed{0%,100%{opacity:.35;transform:translateX(0)}45%{opacity:1;transform:translateX(14px)}70%{opacity:.65;transform:translateX(0)}}@keyframes dash{to{stroke-dashoffset:-152}}@keyframes spinA{to{transform:rotate(360deg)}}@keyframes spinB{to{transform:rotate(-360deg)}}@keyframes wake{0%,8%,100%{opacity:.48;transform:scale(1)}14%,20%{opacity:1;transform:scale(1.025)}}@keyframes stagePulse{0%,100%{opacity:.62}12%,20%{opacity:1}36%,44%{opacity:1}60%,68%{opacity:1}}@keyframes toolPulse{0%,100%{opacity:.62}16%,22%{opacity:1}38%,44%{opacity:1}62%,70%{opacity:1}82%,90%{opacity:1}}@keyframes trace{0%,11%{stroke-dasharray:0 700}78%,100%{stroke-dasharray:700 0}}
  @media (prefers-reduced-motion: reduce){.breathe,.seed,.signalPath,.signalPathSlow,.irisA,.irisB,.wake,.stagePulse,.toolPulse,.trace{animation:none!important;transform:none!important;opacity:1!important}}
`;

const logoSpecs = [
  ["figma", "Figma", "siFigma"],
  ["linear", "Linear", "siLinear"],
  ["notion", "Notion", "siNotion"],
  ["react", "React", "siReact"],
  ["swiftui", "SwiftUI", "siSwift"],
  ["firebase", "Firebase", "siFirebase"],
  ["claude", "Claude", "siClaude"],
  ["github", "GitHub", "siGithub"],
];

function out(file) {
  return path.join(root, file);
}

function ensureDir(file) {
  fs.mkdirSync(path.dirname(out(file)), { recursive: true });
}

function write(file, value) {
  ensureDir(file);
  fs.writeFileSync(out(file), value.trimStart(), "utf8");
  console.log(`wrote ${file}`);
}

function esc(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
}

function svg({ width, height, title, desc, body, style = "", defs = "" }) {
  const defsBlock = defs ? `  ${defs}\n` : "";
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title desc">
<title id="title">${esc(title)}</title>
<desc id="desc">${esc(desc)}</desc>
<defs>
  <linearGradient id="mineralWash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#F5F8F4"/><stop offset=".62" stop-color="#E9F0EA"/><stop offset="1" stop-color="#DCE8DE"/></linearGradient>
  <linearGradient id="bioPanel" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#06110B"/><stop offset=".58" stop-color="#0A1A11"/><stop offset="1" stop-color="#102419"/></linearGradient>
  <radialGradient id="irisGlow" cx="50%" cy="50%" r="56%"><stop stop-color="#102419"/><stop offset=".68" stop-color="#06110B"/><stop offset="1" stop-color="#53E786" stop-opacity=".16"/></radialGradient>
${defsBlock}
  <style>${tokenCss}${style}</style>
</defs>
${body}
</svg>`;
}

function panel(x, y, w, h, label, children = "") {
  return `<g transform="translate(${x} ${y})">
  <path class="panel" d="M18 0H${w - 18}L${w} 18V${h - 18}L${w - 18} ${h}H18L0 ${h - 18}V18Z"/>
  <text class="mono micro" x="28" y="42" font-size="18" fill="#95F5B4">${label}</text>
  <path class="line" d="M28 60H${w - 28}" opacity=".55"/>
  ${children}
</g>`;
}

function hero(animated) {
  const style = animated ? motionCss : "";
  const cls = animated ? " signalPath" : "";
  const body = `
<rect width="1600" height="900" fill="url(#mineralWash)"/>
<path class="shell" d="M34 34H450L468 54H1134L1152 34H1566V866H34Z" opacity=".92"/>
<path class="line" d="M72 96C264 84 382 124 500 238S760 286 910 220s288-70 468 16" opacity=".42"/>
<g transform="translate(82 110)">
  <path d="M0 0H478L510 32V424L478 456H0Z" fill="#F9FCF8" stroke="#B9CCBE"/>
  <g class="${animated ? "wake" : ""}" transform="translate(28 28)">
    <path d="M18 0C8 4 0 15 0 29c0 20 18 35 18 35s18-15 18-35C36 15 28 4 18 0Z" fill="none" stroke="#13743F" stroke-width="2"/>
    <circle cx="12" cy="28" r="3" fill="#13743F"/><circle cx="24" cy="28" r="3" fill="#13743F"/><path d="M10 43c6 5 10 5 16 0" class="signal" stroke-width="2"/>
  </g>
  <text class="sans title label" x="28" y="142" font-size="68" font-weight="650">Yash Kanadhia</text>
  <text class="sans small" x="31" y="190" font-size="24" fill="#13743F" font-weight="650">Product Designer</text>
  <text class="sans muted" x="31" y="236" font-size="25">Toronto, Ontario, Canada</text>
  <path d="M31 280H122" class="signal" stroke-width="3"/>
  <text class="sans label" x="31" y="336" font-size="31">I design and build systems that</text>
  <text class="sans label" x="31" y="380" font-size="31">connect people to outcomes.</text>
</g>
<g transform="translate(660 120)">
  <circle cx="340" cy="245" r="128" fill="url(#irisGlow)" stroke="#13743F" stroke-width="1.5"/>
  <g class="${animated ? "irisA" : ""}"><path class="signal" d="M340 90a155 155 0 0 1 140 88M494 260a155 155 0 0 1-114 134M212 284a155 155 0 0 1 3-120" stroke-width="5"/></g>
  <g class="${animated ? "irisB" : ""}"><path class="softSignal" d="M340 130a115 115 0 0 1 92 46M448 258a115 115 0 0 1-73 87M248 288a115 115 0 0 1-2-94" stroke-width="2.5"/></g>
  <circle cx="340" cy="245" r="48" fill="#06110B" stroke="#95F5B4"/>
  <path class="signal${cls}" d="M-28 560C136 480 208 360 340 245S640 126 818 84" opacity=".72" stroke-width="2.5"/>
</g>
${panel(910, 108, 548, 170, "ZEREF", `<text class="mono darkText" x="32" y="92" font-size="18">zeref = { memory: "local-first",</text><text class="mono darkText" x="32" y="124" font-size="18">  context: "guarded", handoffs: "cross-harness" }</text><circle class="${animated ? "seed" : ""} node" cx="500" cy="108" r="8"/>`)}
${panel(910, 306, 548, 170, "PERFIN OS", `<text class="mono darkText" x="32" y="92" font-size="18">perfin = { ownership: "team project",</text><text class="mono darkText" x="32" y="124" font-size="18">  platform: "React Native + Firebase" }</text><circle class="${animated ? "seed" : ""} node" cx="500" cy="108" r="8"/>`)}
<g transform="translate(620 534)">
  <path class="shell" d="M18 0H810L828 18V112L810 130H18L0 112V18Z" fill="#F9FCF8"/>
  ${metric(42, "2", "Ready to Ship Projects", animated, "0s")}
  <path class="line" d="M296 26V104"/>
  ${metric(330, "1", "Team Project", animated, "2s")}
  <path class="line" d="M562 26V104"/>
  ${metric(598, "5", "Certificates", animated, "4s")}
</g>
<g transform="translate(58 752)">
  <path class="shell" d="M18 0H1466L1484 18V92L1466 110H18L0 92V18Z" fill="#F9FCF8"/>
  <path class="signal${cls}" d="M54 55H1428" opacity=".28"/>
  ${toolRailText(78, 62)}
</g>`;
  return svg({
    width: 1600,
    height: 900,
    title: animated ? "Yash Kanadhia Organic AlienTech motion hero" : "Yash Kanadhia Organic AlienTech static hero",
    desc: "Profile hero for Yash Kanadhia with locked identity, Zeref and PerFin OS panels, three profile metrics, nine tools, a restrained system glyph, and a central iris motif.",
    style,
    body,
  });
}

function metric(x, n, label, animated, delay) {
  const anim = animated ? `stagePulse" style="animation-delay:${delay}` : "";
  return `<g class="${anim}" transform="translate(${x} 32)"><circle class="node" cx="24" cy="28" r="21" opacity=".72"/><text class="sans label" x="62" y="40" font-size="22"><tspan font-size="44" font-weight="700" fill="#13743F">${n}</tspan> ${label}</text></g>`;
}

function toolRailText(x, y) {
  const tools = ["Figma", "Linear", "Notion", "React", "SwiftUI", "Firebase", "Claude", "Codex", "GitHub"];
  return tools.map((name, i) => `<text class="sans label" x="${x + i * 152}" y="${y}" font-size="18">${name}</text>`).join("");
}

function openAiPath() {
  const value = fs.readFileSync(out("node_modules/bootstrap-icons/icons/openai.svg"), "utf8").match(/<path[^>]*d="([^"]+)"/)?.[1];
  if (!value) throw new Error("Missing Bootstrap OpenAI path");
  return value;
}

function toolMark(name) {
  const map = {
    Figma: ["siFigma", 24],
    Linear: ["siLinear", 24],
    Notion: ["siNotion", 24],
    React: ["siReact", 24],
    SwiftUI: ["siSwift", 24],
    Firebase: ["siFirebase", 24],
    Claude: ["siClaude", 24],
    GitHub: ["siGithub", 24],
  };
  if (name === "Codex") return `<g transform="translate(-19 -19) scale(2.35)"><path fill="#13743F" d="${openAiPath()}"/></g>`;
  const [key] = map[name];
  const icon = icons[key];
  return `<g transform="translate(-18 -18) scale(1.5)"><path fill="#13743F" d="${icon.path}"/></g>`;
}

function constellation(animated) {
  const style = animated ? motionCss : "";
  const tools = [
    ["Figma", 160, 180], ["Linear", 314, 250], ["Notion", 468, 180],
    ["React", 680, 255], ["SwiftUI", 842, 180], ["Firebase", 1004, 255],
    ["Claude", 1196, 180], ["Codex", 1330, 260], ["GitHub", 1464, 180],
  ];
  const nodes = tools.map(([name, x, y], i) => `<g class="${animated ? "toolPulse" : ""}" style="animation-delay:${i * .55}s" transform="translate(${x} ${y})"><circle cx="0" cy="0" r="48" fill="#F9FCF8" stroke="#B9CCBE"/>${toolMark(name)}<circle cx="0" cy="0" r="7" class="node" opacity=".72"/><text class="sans label" y="80" text-anchor="middle" font-size="18">${name}</text></g>`).join("");
  const body = `
<rect width="1600" height="640" fill="url(#mineralWash)"/>
<path class="shell" d="M34 34H1566V606H34Z"/>
<text class="sans title label" x="70" y="92" font-size="42" font-weight="650">Product and delivery tool constellation</text>
<text class="mono micro muted" x="72" y="132" font-size="18">DISCOVER -> ORGANIZE -> DESIGN -> BUILD -> VERIFY -> SHIP</text>
<path class="signal${animated ? " signalPath" : ""}" d="M160 180C270 70 370 330 468 180S592 354 680 255S782 72 842 180S902 350 1004 255S1104 100 1196 180S1268 340 1330 260S1400 70 1464 180" stroke-width="3"/>
<path class="softSignal${animated ? " signalPathSlow" : ""}" d="M160 180H468M680 255H1004M1196 180H1464" opacity=".55" stroke-width="2"/>
${nodes}
<g transform="translate(1180 490)"><path class="panel" d="M16 0H330L346 16V70L330 86H16L0 70V16Z"/><text class="mono" x="32" y="54" font-size="22" fill="#95F5B4">EVIDENCE RECORDED</text></g>`;
  return svg({ width: 1600, height: 640, title: animated ? "AlienTech tool constellation motion" : "AlienTech tool constellation static", desc: "Workflow constellation connecting Figma, Linear, Notion, React, SwiftUI, Firebase, Claude, Codex, and GitHub in approved order.", style, body });
}

function zerefFlow(animated) {
  const style = animated ? motionCss : "";
  const labels = ["CONTEXT", "EVIDENCE CLASSIFICATION", "PRIVACY CHECK", "CONTRADICTION CHECK", "GUARDED WRITE", "AUDIT TRACE", "CROSS-TOOL HANDOFF"];
  const boxes = labels.map((label, i) => {
    const x = i % 2 === 0 ? 190 : 855;
    const y = 120 + i * 72;
    return `<g class="${animated ? "stagePulse" : ""}" style="animation-delay:${i * .7}s" transform="translate(${x} ${y})"><path class="panel" d="M16 0H500L516 16V60L500 76H16L0 60V16Z"/><text class="sans darkText" x="258" y="47" text-anchor="middle" font-size="22" font-weight="650">${label}</text></g>`;
  }).join("");
  const body = `
<rect width="1600" height="680" fill="url(#mineralWash)"/>
<path class="shell" d="M34 34H1566V646H34Z"/>
<text class="sans title label" x="70" y="82" font-size="38" font-weight="650">Zeref guarded-memory flow</text>
<path class="signal${animated ? " trace" : ""}" d="M706 168C770 194 805 196 856 224C925 262 718 280 706 338C694 397 824 404 856 452C890 504 720 520 706 548C694 584 930 596 1210 598" stroke-width="3"/>
${boxes}
<circle class="${animated ? "seed" : ""} node" cx="708" cy="168" r="10"/>
<text class="mono muted" x="970" y="604" font-size="17">append-only handoff exits for human review</text>`;
  return svg({ width: 1600, height: 680, title: animated ? "Zeref guarded-memory flow motion" : "Zeref guarded-memory flow static", desc: "Seven-stage Zeref flow: context, evidence classification, privacy check, contradiction check, guarded write, audit trace, and cross-tool handoff.", style, body });
}

function workingModel(animated) {
  const style = animated ? motionCss : "";
  const stages = ["FRAME", "MODEL", "DESIGN", "BUILD", "VERIFY", "COMMUNICATE"];
  const nodes = stages.map((name, i) => {
    const x = 150 + i * 260;
    return `<g class="${animated ? "stagePulse" : ""}" style="animation-delay:${i * .75}s" transform="translate(${x} 230)"><circle cx="0" cy="0" r="58" fill="#F9FCF8" stroke="#B9CCBE"/><circle cx="0" cy="0" r="10" class="node"/><text class="sans label" y="94" text-anchor="middle" font-size="21" font-weight="650">${name}</text></g>`;
  }).join("");
  const body = `
<rect width="1600" height="520" fill="url(#mineralWash)"/>
<path class="shell" d="M34 34H1566V486H34Z"/>
<text class="sans title label" x="70" y="90" font-size="40" font-weight="650">Product working model</text>
<path class="signal${animated ? " signalPath" : ""}" d="M150 230H1450" stroke-width="3"/>
<path class="softSignal${animated ? " signalPathSlow" : ""}" d="M1450 304C1160 430 480 430 150 304" stroke-width="2" opacity=".72"/>
${nodes}
<text class="mono muted" x="1180" y="410" font-size="18">documented output returns learning to Frame</text>`;
  return svg({ width: 1600, height: 520, title: animated ? "Product working model motion" : "Product working model static", desc: "Six-stage working model: Frame, Model, Design, Build, Verify, and Communicate with a feedback filament.", style, body });
}

function badge(label) {
  const text = label.toUpperCase().replaceAll("-", " ");
  return svg({ width: 420, height: 110, title: `${text} badge`, desc: `Static evidence badge labeled ${text}.`, body: `<rect width="420" height="110" rx="0" fill="#F5F8F4"/><path class="shell" d="M16 16H404V94H16Z"/><circle class="node" cx="58" cy="55" r="14"/><path class="signal" d="M50 55l6 7 14-18" stroke-width="3"/><text class="sans label" x="92" y="64" font-size="24" font-weight="650">${text}</text>` });
}

function sectionHeader(label, title) {
  return svg({ width: 1200, height: 180, title: `${title} section header`, desc: `Static Organic AlienTech section header for ${title}.`, body: `<rect width="1200" height="180" fill="url(#mineralWash)"/><path class="shell" d="M22 22H1178V158H22Z"/><text class="mono micro muted" x="58" y="62" font-size="17">${label}</text><text class="sans title label" x="58" y="116" font-size="42" font-weight="650">${title}</text><path class="signal" d="M840 90C918 44 1040 44 1120 90" stroke-width="2"/><circle class="node" cx="1124" cy="90" r="8"/>` });
}

function placeholder(project) {
  return svg({ width: 1600, height: 900, title: `${project} product media parked`, desc: "Reserved media placeholder. Product proof is not fabricated.", body: `<rect width="1600" height="900" fill="url(#mineralWash)"/><path class="shell" d="M46 46H1554V854H46Z"/><path class="panel" d="M160 250H1440V650H160Z"/><text class="mono micro" x="800" y="398" text-anchor="middle" font-size="28" fill="#95F5B4">PRODUCT MEDIA PARKED</text><text class="sans darkText" x="800" y="468" text-anchor="middle" font-size="34" font-weight="650">TEXT AND EVIDENCE REMAIN AVAILABLE BELOW</text><text class="sans darkText" x="800" y="532" text-anchor="middle" font-size="28">${project}</text><path class="signal" d="M300 600C520 540 690 615 800 560S1080 520 1300 600" opacity=".65" stroke-width="3"/>` });
}

function socialSvg() {
  return svg({ width: 1280, height: 640, title: "Yash Kanadhia GitHub profile social preview", desc: "Social preview for Yash Kanadhia's GitHub profile.", body: `<rect width="1280" height="640" fill="url(#mineralWash)"/><path class="shell" d="M38 38H1242V602H38Z"/><circle cx="964" cy="244" r="120" fill="url(#irisGlow)" stroke="#13743F"/><path class="signal" d="M845 244a120 120 0 0 1 180-104M1084 250a120 120 0 0 1-148 110" stroke-width="5"/><text class="sans title label" x="90" y="218" font-size="78" font-weight="650">Yash Kanadhia</text><text class="sans" x="94" y="288" font-size="36" fill="#13743F" font-weight="650">Product Designer</text><text class="sans muted" x="94" y="370" font-size="31">Product systems · AI-assisted delivery · Inspectable evidence</text>` });
}

function writeLogos() {
  const rows = [];
  for (const [slug, label, key] of logoSpecs) {
    const icon = icons[key];
    if (!icon) throw new Error(`Missing simple-icons entry ${key}`);
    const svgLogo = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 24 24" role="img" aria-labelledby="title desc">
<title id="title">${label} logo</title><desc id="desc">${label} logo sourced from simple-icons ${icon.source || "catalog"}.</desc>
<path fill="#${icon.hex}" d="${icon.path}"/>
</svg>`;
    write(`assets/tooling/logos/${slug}.svg`, svgLogo);
    rows.push([label, `simple-icons ${icon.title}`, icon.source || "https://simpleicons.org/", "CC0-1.0 package; brand trademarks retained by owners", today, "Scaled through SVG viewBox only; color uses Simple Icons brand hex."]);
  }
  write("assets/tooling/logos/codex.svg", `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 16 16" role="img" aria-labelledby="title desc">
<title id="title">Codex logo</title><desc id="desc">OpenAI mark used for Codex, sourced from Bootstrap Icons and documented against OpenAI brand guidance.</desc>
<path fill="#13241A" d="${openAiPath()}"/>
</svg>`);
  rows.push(["Codex", "OpenAI mark via Bootstrap Icons", "https://icons.getbootstrap.com/icons/openai/ and https://openai.com/brand/", "MIT for vendored path; OpenAI brand/trademark rights retained by OpenAI", today, "Used as the Codex product mark because no separate verified Codex icon ships in Simple Icons."]);
  write("docs/visual-system/logo-sources.md", `# Logo Sources

Retrieval date: ${today}

These logo files are vendored locally for GitHub README rendering. No README SVG depends on remote logo files.

| Logo | Source used | Source URL | License and rights | Retrieval date | Modification |
|---|---|---|---|---|---|
${rows.map((r) => `| ${r.map(esc).join(" | ")} |`).join("\n")}
`);
}

function main() {
  write("assets/hero/yash-kanadhia-alientech-motion.svg", hero(true));
  write("assets/hero/yash-kanadhia-alientech-static.svg", hero(false));
  write("assets/tooling/alientech-tool-constellation-motion.svg", constellation(true));
  write("assets/tooling/alientech-tool-constellation-static.svg", constellation(false));
  write("assets/motion/zeref-system-flow-motion.svg", zerefFlow(true));
  write("assets/motion/zeref-system-flow-static.svg", zerefFlow(false));
  write("assets/motion/product-working-model-motion.svg", workingModel(true));
  write("assets/motion/product-working-model-static.svg", workingModel(false));
  writeLogos();

  for (const name of ["verified", "documented", "team-project", "independent", "prototype", "simulated", "known-boundary", "media-parked"]) write(`assets/ui/badges/${name}.svg`, badge(name));
  const headers = [["overview", "OVERVIEW", "Overview"], ["selected-work", "SELECTED WORK", "Selected Work"], ["capabilities", "CAPABILITIES", "Capabilities"], ["evidence", "EVIDENCE", "Evidence"], ["how-i-work", "HOW I WORK", "How I Work"], ["stack", "STACK", "Stack"], ["current-signals", "CURRENT SIGNALS", "Current Signals"], ["connect", "CONNECT", "Connect"]];
  for (const [file, label, title] of headers) write(`assets/ui/sections/${file}.svg`, sectionHeader(label, title));
  for (const [file, title] of [["zeref", "Zeref Memory Engine"], ["perfin", "PerFin OS"], ["for-rent", "For Rent"], ["streamnexus", "StreamNexus"]]) write(`assets/project-portals/${file}-media-parked.svg`, placeholder(title));
  write("assets/social/github-profile-og.svg", socialSvg());
}

main();
