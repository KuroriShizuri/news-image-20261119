# The World Today — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/KuroriShizuri/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/KuroriShizuri/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for make.fun competition `news-image-20261119`: sum up 19 November's
world news in one image.

`main.py` (Python 3.13, stdlib only, no network) copies the bundled
cover artwork `entry.png` (1024×1024 PNG, 188,722 bytes — under the
1 MiB limit) to `<MAKEFUN_OUTPUT_DIR>/entry.png` (`/output` by default).
Before copying it checks the source image's magic bytes (JPEG or PNG),
validates the dimensions are exactly 1024×1024, and prints a confirmation
line with the byte count. The copy is byte-identical on every run, verified
afterwards by file size and SHA-256 digest.

## What the cover shows

The design borrows the grammar of The Economist's *The World Ahead 2027*
cover (17 November 2026, art by Cleon Peterson) — one crowded round globe,
packed with tiny flat silhouettes, vertical hierarchy, forces rather than
people — but the composition is its own: seven numbered hero vignettes,
each at least 170×170 px, each carrying one story with one unmistakable
icon, a numbered red medallion (1–7), and a short label in condensed bold
type. No story depends on the crowd; the crowd is filler between the
vignettes. The wording is hedged where the news is prospective:
"SET TO BE", "PROPOSES", "NEARS".

The artwork is built as vector SVG by code and rendered to PNG at exactly
1024×1024 — every word is real typeset text, never rendered by an image
model. Palette: flat red, black, white and light grey, with exactly three
exceptions where flag correctness wins over palette purity — Russia's
white-blue-red, the EU's blue field with gold stars, and Ukraine's
blue-yellow. There are no gradients anywhere: the cyclone is a single
flat black spiral stroke with one flat red arc, verified by palette count
(the cyclone region is 93% exactly white, black and red pixels; the rest
are anti-aliasing edge pixels, not shading). Full design philosophy:
`design-philosophy.md` in the build notes.

Researched from the day's reporting (19 November 2026):

1. **GTA VI launches worldwide** — after a 13-year wait, the game is out
   and gamers enter Vice City; pre-order records broken. Shown as a neon
   sunset over a Vice City skyline, palms, a game controller, and a "VI"
   mark — the hero vignette at the top of the globe.
2. **Jeffries set to be first Black Speaker** — Democrats nominate Hakeem
   Jeffries for Speaker of the US House of Representatives. Shown as a
   flat black Capitol dome with white incised lines, gavel and rostrum.
3. **US and Iran trade fire again** — Iran widens its attacks on US sites
   in the Gulf, striking Bahrain and Kuwait; the US hit a missile site on
   Qeshm Island. Shown as two warships with tracer arcs and muzzle
   flashes in both directions — an exchange, not a one-sided barrage.
4. **Trump, Xi and Putin meet in Shenzhen** — the three leaders sit down
   together for the first time, at the APEC summit. Shown as three large
   suited figures at a table before a skyline, under the US, Chinese and
   Russian flags (drawn in their correct colours).
5. **EU proposes €45bn Ukraine loan** — to be repaid only once Russia pays
   reparations; otherwise frozen Russian assets may be used. Shown as a
   ring of 12 gold stars on a blue field, a gold € sign, an arrow into a
   blue-and-yellow Ukraine outline, and coin stacks.
6. **Voyager 1: one light-day from Earth** — the first human-made object
   to reach the mark, 16 billion miles out; a radio signal now takes a
   full day each way. Shown as a flat dish-and-boom spacecraft outside
   the globe in the void, a beam of light to a small Earth, and a
   "1 LIGHT-DAY" distance marker.
7. **Cyclone Akvan nears India's east coast** — a severe cyclonic storm in
   the Bay of Bengal; red alerts for coastal Andhra Pradesh and Odisha
   on 19–20 November, landfall expected around noon on 20 November.
   Shown as a flat black spiral with a red arc — no gradient, no
   feathering.

## Verification

- PNG exactly 1024×1024, 188,722 bytes (limit 1,048,576).
- Palette: 3,412 distinct colours in total (flat art plus anti-aliasing
  edge pixels); dominant colours are the paper (239,239,233), white,
  black and red, plus the three flag colours. Cyclone region: 93.3% of
  pixels are exactly white, black or red — no continuous grey ramp.
- Downscale check: all 7 stories still identifiable from symbols +
  labels at 512×512 and at 300×300 (labels stay legible; medallions
  1–7 stay visible).
- `python3 entry/main.py` runs and the output is byte-identical to the
  bundled image (SHA-256
  `e3db5ea294ab85d8020ad15b5b0cb546b851ecd21466b72e2fb53cc69c2ca9b1`).
- Every on-image text line spell-checked by eye at full size; date
  "Thursday 19 November 2026" is correct.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1g7byhvf&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
