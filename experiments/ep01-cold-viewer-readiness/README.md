# EP01 Cold-Viewer YouTube Readiness Experiment

**EXPERIMENTAL_EVIDENCE_NOT_GOVERNANCE**

A blinded editorial experiment testing whether a proposed first YouTube episode script functions for a cold viewer — one with no prior relationship to the creator. Run 2026-08-10.

These files record experimental evidence only. They are **not** a governance decision, an approval, a publication state, or narration authority, and they alter no existing artifact.

## Result

**Disposition: READY_WITH_BOUNDED_CUTS** — one of five dispositions frozen before the script was exposed to any evaluator.

Headline findings: 7/7 evaluators continued at every sequential checkpoint and finished the episode. Zero FAIL ratings on any of twenty criteria. One unanimous WEAK (repetition). The minimum change capable of moving the script to READY is about 57 words cut plus two relocations, with no new substantive prose.

Start with **`00-VERDICT.md`**.

## Method

1. **Freeze first.** A twenty-criterion instrument with STRONG/ADEQUATE/WEAK/FAIL anchors, aggregation thresholds, and five dispositions with mechanical decision rules was written and hashed *before* any evaluative reading (`01-frozen-instrument.md`, sha256 `42d084ec…`). It was not modified afterward.
2. **Seven independent cold viewers**, each in an isolated context, each a distinct viewing condition (housing-intent, adjacent-interest, skeptical, impatient, analytical, low-financial-literacy, story-first). None saw another's assessments.
3. **True sequential exposure.** The script was delivered in six segments across separate turns at 150 wpm nominal. At each checkpoint the evaluator's context contained only what had been seen so far, so later material could not contaminate earlier answers.
4. **Recall test** administered without re-showing the script.
5. **Attention map** — all 60 passages labelled PULL / CARRY / FRICTION / EXIT_RISK by each evaluator independently, aggregated at pre-frozen thresholds (≥4/7 pull, ≥3/7 friction, ≥2/7 exit risk).
6. **Adversary**, instantiated only after all seven runs completed, given the script and passage IDs and nothing else — no viewer data. Its findings were admitted only where viewer evidence corroborated them; three were rejected on that basis.
7. **Season-arc evaluator**, a fresh context given the ten-episode season fact. Its results are reported separately and could not change any cold-viewer score.

## Files

| File | Contents |
|---|---|
| `00-VERDICT.md` | Phase IX verdict, sections A–K. **Read this first.** |
| `01-frozen-instrument.md` | The instrument, frozen and hashed before exposure |
| `02-input-script-passaged.md` | Canonical transcription with passage IDs P01–P60 |
| `04-viewer-survival.md` | Continuation counts and per-checkpoint tallies |
| `05-attention-map.md` | Aggregated attention map, cadence probe, criterion medians |
| `05a-attention-aggregate-raw.txt` | Raw aggregation output |
| `06-recall.md` | Recall results, factual and conceptual scored separately |
| `07-minimum-change.md` | Minimum-change prescription; adversary claims tested against viewer data |
| `07a-adversary.md` | Adversary output, verbatim |
| `08-disposition-derivation.md` | Mechanical application of the frozen decision rules |
| `09-season-arc.md` | Season-function assessment, verbatim |
| `99-run-log.md` | Method notes, timing, and incidents |
| `evaluators/viewer-1..7.md` | All seven evaluators' outputs, verbatim, preserved before aggregation |
| `aggregate.py` | The aggregation script (reproduces `05a` from the evaluator files) |

## Contamination control

No repository history, prior scripts, prior audits, production artifacts, or other Calculated Landlord material was read at any point. No comparison was made against another version. No subscriber counts, channel history, production investment, or prior judge results informed any result. The only repository operations were creating this directory and adding these new files.

Two limitations are recorded rather than hidden: the script arrived in the same message as the experiment brief, so orchestrator-level literal blindness was impossible (the instrument was therefore built generically from the brief's criterion list and hashed before exposure); and evaluator agents retain transcript context, so the recall phase measures immediate-impression retention plus structural-memorability judgment rather than literal forgetting. Both are stated in `01-frozen-instrument.md` and `99-run-log.md`.
