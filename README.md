# tiny-chess-01 — v8

Strongest-chess-engine-in-4KB entry: a single-file Python 3.13 stdlib
engine (`main.py`, 4,090 bytes) driving the make.fun env
(`POST /game`, `/move`, `/resign`). Deterministic: fixed 90,000-node
budget per move, iterative deepening, no clock, no randomness, no network
except the env itself.

## Engine

- 0x88 board, alpha-beta + quiescence (captures, 6 plies, check evasions
  and check extensions), transposition table, killer moves, MVV-LVA
  move ordering, iterative deepening with best-move-first reordering.
- v8 changes vs v7 (4,095 B, trial-0 Elo 1,396):
  - **LMR**: late (4th+) quiet moves at depth > 2, not in check, are
    searched one ply shallower. Measured locally: +1 completed ply on
    3 of 6 bench positions (start 5→6, Ruy 4→5, QGD 4→5) at the same
    90k-node cap, same depth on the other 3.
  - **Tempo**: +10 cp for the side to move at quiescence leaf and
    stand-pat (three sites, applied consistently).
  - **Speed golf** (same search, less per-node cost): `enumerate` move
    generation, cached `abs(p)` in make, bare-tuple literals, `and`
    king-guard in eval, negative-key sort instead of `reverse=1`,
    `bm.__ne__` root reordering, `a%4==2` slider break. Profiled
    ~2% faster per node than v7 at the same 90k budget.
  - Node budget kept at **90,000/move**: the speed/LMR gains are banked
    as wall-time margin (v7's production wall estimate was already
    1,500–1,650 s of the 1,800 s limit), not spent on more nodes.
- Eval: sunfish-style piece-square tables (base85-packed), material
  values 100/280/320/479/929, bishop-pair +30/-30, tempo +10.

## Verification (local, Python 3.12)

- perft from start: 20 / 400 / 8,902 / 197,281 (exact).
- Mate-in-1 (Scholar's mate) found; castling, en-passant and all four
  promotions verified; bishop-pair +30/-30 and make/unmake round-trip
  verified; no `time`/`random` imports; parses clean.
- Bench (5 positions, 90k nodes each): ~34,900 nodes/s mean.
- Local trial-0: see `~/workspace/makefun/trial0-v8/` (run log, scores).

## Files

- `main.py` — the engine (4,090 bytes, ≤ 4,096).
- `LICENSE` — MIT, SPDX tag only.
- `.makefun/owner.json` — payout wallet.
