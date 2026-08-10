#!/usr/bin/env python3
"""Aggregate the seven independent attention maps and criterion ratings.

Applies the thresholds frozen in 00-frozen-instrument.md sec 0:
  consensus FRICTION  >= 3/7 marking FRICTION or EXIT_RISK
  consensus EXIT_RISK >= 2/7 marking EXIT_RISK
  consensus PULL      >= 4/7 marking PULL
Criterion aggregate = median of seven (STRONG=3, ADEQUATE=2, WEAK=1, FAIL=0).
"""
import re
import pathlib
import statistics

RAW = pathlib.Path(__file__).parent / "viewers" / "raw"
VIEWERS = [1, 2, 3, 4, 5, 6, 7]
SCALE = {"STRONG": 3, "ADEQUATE": 2, "WEAK": 1, "FAIL": 0}
UNSCALE = {3: "STRONG", 2: "ADEQUATE", 1: "WEAK", 0: "FAIL"}

maps, crits, cadence = {}, {}, {}
missing = []

for v in VIEWERS:
    path = RAW / f"v{v}-map.md"
    if not path.exists():
        missing.append(v)
        continue
    text = path.read_text()
    body = text.split("OUTPUT PART 3")[0]
    maps[v] = {m.group(1): m.group(2)
               for m in re.finditer(r"^(P\d\d): (PULL|CARRY|FRICTION|EXIT_RISK)", body, re.M)}
    cm = re.search(r"^CADENCE: (YES|SOMEWHAT|NO)", text, re.M)
    cadence[v] = cm.group(1) if cm else "?"
    # two observed formats: "C01 Label: STRONG — ..." and "C01 STRONG — ..."
    crits[v] = {m.group(1): m.group(2)
                for m in re.finditer(
                    r"^(C\d\d)(?:[^:\n]*:)?\s*(STRONG|ADEQUATE|WEAK|FAIL)\b", text, re.M)}

print(f"maps parsed: {sorted(maps)}   missing: {missing}")
for v in sorted(maps):
    print(f"  V{v}: {len(maps[v])} passages, {len(crits[v])} criteria, cadence={cadence[v]}")
if missing:
    raise SystemExit("\nIncomplete — rerun when all seven maps are saved.")

print("\n=== CONSENSUS ATTENTION MAP (frozen thresholds) ===")
rows = []
for i in range(1, 61):
    p = f"P{i:02d}"
    labels = [maps[v].get(p, "?") for v in VIEWERS]
    n_pull = labels.count("PULL")
    n_exit = labels.count("EXIT_RISK")
    n_fric = labels.count("FRICTION") + n_exit
    flags = []
    if n_pull >= 4:
        flags.append(f"PULL({n_pull}/7)")
    if n_exit >= 2:
        flags.append(f"EXIT_RISK({n_exit}/7)")
    if n_fric >= 3:
        flags.append(f"FRICTION({n_fric}/7)")
    rows.append((p, n_pull, n_fric, n_exit, flags))
    if flags:
        print(f"{p}  {' '.join(flags):<45} raw: {','.join(labels)}")

print("\n--- sub-threshold but notable (2 friction, or 1 exit-risk) ---")
for p, n_pull, n_fric, n_exit, flags in rows:
    if not flags and (n_fric == 2 or n_exit == 1):
        print(f"{p}  friction={n_fric} exit={n_exit}")

print("\n=== CRITERION MEDIANS ===")
for i in range(1, 21):
    c = f"C{i:02d}"
    vals = [SCALE[crits[v][c]] for v in VIEWERS if c in crits[v]]
    if len(vals) != 7:
        print(f"{c}: incomplete ({len(vals)}/7)")
        continue
    med = int(statistics.median(sorted(vals)))
    dist = {k: sum(1 for x in vals if x == SCALE[k]) for k in SCALE}
    dstr = " ".join(f"{k[0]}{n}" for k, n in dist.items() if n)
    print(f"{c}: median={UNSCALE[med]:<9} [{dstr}]")

print("\n=== CADENCE PROBE ===")
for v in VIEWERS:
    print(f"  V{v}: {cadence[v]}")
print("  tally:", {k: sum(1 for x in cadence.values() if x == k) for k in ("YES", "SOMEWHAT", "NO")})
