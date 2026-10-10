# MEASUREMENTS_NEEDED.md

Physical inputs this design assumed or deferred. Rev 2 should fold each
answer back into `cad/parameters.py` and re-run `scripts/validate.py`.

| # | Unknown | Current assumption | How to measure | Blocks |
|---|---|---|---|---|
| 1 | Battery cell L × W × T | 30 × 22 × 6.0 mm (LP-series-ish placeholder) | calipers on the chosen protected 1S cell | pocket fit, bump depth, case thickness |
| 2 | Battery wire gauge + JST harness length | 2 × Ø1.3, PH housing rear exit at 2.0 mm | calipers + the real harness | wire lane, service bay reach |
| 3 | NFC range, closed case (coil + lid + battery) | unknown (hardware repo's own open item) | card + PN7160 read-log distance, lid on, battery in | rev-2 wall/floor thinning |
| 4 | NFC impact of the V2 glass over part of the coil rule area | dielectric, tolerated | repeat measurement 3 with the glass fitted | V2 viability as-is |
| 5 | OLED glass outline | 57.5 (u-long) × 29.4 × 1.9 mm (2.42" SSD1309 candidate, LANDSCAPE) | calipers on the real glass (QDtech OLED242W ordering code unconfirmed in the repo) | window + deck size |
| 6 | NFP1309-02Y flex length + contact-edge side | 12 mm assumed; flex on the +v short edge, design plans a 25 mm FFC jumper | measure the flex; confirm which short edge carries the 24 contacts; buy a 24-way 0.5 mm jumper | display assembly |
| 7 | ESP32-C3 TRP with the open wall window | expected better than closed wall | range/throughput test vs bare board | keep/discard the window |
| 8 | Mouse-bite remnant geometry after the user's cut | ≤2.0 mm stub, ±0.30 spread | calipers after the first real separation | end-wall gap, stop-rib windows |
| 9 | Snap-tab retention force | unmeasured | pull test on the first print | tab count/size |
| 10 | Lip bite feel on the real 1.6 mm laminate | 0.65 mm overhang, 1.1 mm lip | coupon bay C squeeze test | RAIL_LIP_OVERHANG |
| 11 | USB plug boots in the wild | 13.0 × 6.5 envelope + 0.6 clearance | plug 3-5 common cables fully | opening size |
| 12 | Charge-LED visibility through the V2 deck hole | dim (3+ mm deep hole) | eyeball with the board powered | LED window shape / light pipe |
| 13 | J3 blister usability with a real keypad cable | hatch 26 × 5.5 mm | dry-fit a 3×4 matrix keypad pigtail (Adafruit PID 3845-class, 7-line + 2 NC) | hatch size |
| 14 | Real keypad outline vs 70×50×7 assumption | Adafruit 1824 datasheet (stand-in basis) | caliper the purchased keypad before printing V4; bay = outline + 0.6 | V4 bay fit |
| 15 | Keypad key pitch / cap size (stand-in cosmetic only) | 10.8×9.2 caps, conservative | measure once a real keypad is at hand; affects renders, not the bay | stand-in fidelity |
| 16 | Fetch the real 1824 STEP | login-gated (GrabCAD adafruit-3x4-phone-style-matrix-keypad-1) | download with an account; replace cad stand-in | render realism |

## Board-side observations (do NOT fix here)

* The JST PH housing (5.6 mm) sets the interior height — a lower battery
  connector on a future PCB rev would drop the case ~3 mm.
* **Board-rev drift (2026-10-09): the nucula-board repo's current rev has
  J2 as a JST SH SM02B side-entry connector opening toward the LEFT edge
  (u=0), not the PH rear-exit this enclosure was extracted from; it also
  adds six M2 holes (four main-board + H5/H6 on the keyboard section) and
  J6 direct battery wire pads.** Re-run `scripts/extract_kicad_geometry.py`
  against the current board before the next print; the battery wire route
  and the left-wall service slot will need re-derivation for a side-entry
  J2.
* The display socket faces the NFC coil; the landscape glass (v ~23.6..53)
  overhangs the coil rule area's lower band (disclosed dielectric). A
  shorter glass or a more keyboard-side flex edge trades display area for
  NFC aperture.
* M2 holes now exist on the board (see drift note); screw bosses remain
  REJECTED while "no metal near the coil" stands — revisit only with
  plastic screws or a board rev that moves the holes clear of rule areas.
