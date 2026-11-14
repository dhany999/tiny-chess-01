# tiny-chess-01 — v20

Strongest-chess-engine-in-4KB entry: a single-file Python 3.13 stdlib
engine (`main.py`, 4,096 bytes) driving the make.fun env
(`POST /game`, `/move`, `/resign`). Deterministic: fixed 90,000-node
budget per move, iterative deepening, no clock, no randomness, no network
except the env itself.

## Engine

- 0x88 board, alpha-beta + quiescence (captures, 6 plies, check evasions
  and check extensions), transposition table, killer moves, MVV-LVA
  move ordering, iterative deepening with best-move-first reordering.
- v20 changes vs v17 (4,061 B, trial-0 Elo 1,598):
  - **King centralization with a MATERIAL gate**: in the eval, when the
    side to move's enemy queen is off the board (`-5*S not in B`), the
    king gets `-(abs(f-3)+abs(r-3))*4` — a penalty growing with distance
    from the centre (0 at d4/e4/d5/e5, -32 at the far corner), i.e. the
    king is pulled toward the centre only once the queens are gone.
    The gate is what makes it work: an earlier castling-rights gate
    (C==0) failed because it opened right after castling, while the
    queen is the piece that punishes a central king. The queen scan is
    short-circuited (`a>5 and ...`), so it runs only on king moves.
  - Funded by three proven-neutral golfs only (no feature removed):
    `sc=-Z;bm=n=0` (-2 B), De Morgan in LMR `not(c or ic)` (-4 B),
    `[-x for x in K]+[0]*8` (-1 B). RFP, killers, MVV-LVA, LMR, tempo,
    delta pruning, bishop-pair all kept. Node budget kept at 90,000/move.
  - Screened and rejected for v20: passed-pawn bonus +24 (trial-0 Elo
    1,396, -202) and +9 (Elo 1,173, -425) — harmful at any dose;
    node cap 9e4 -> 2e5 (Elo 1,396, -202, and wall 2144 s > 1800 s);
    one-reply extension (Elo 1,598, exact tie — never changed a move);
    king-centralization scale *6 (Elo 1,530, -139 vs *4 — overdoes it).
- Eval: sunfish-style piece-square tables (base85-packed), material
  values 100/280/320/479/929, tempo +10.

## Verification (local, Python 3.12)

- perft from start: 20 / 400 / 8,902 / 197,281 (exact).
- Local trial-0: Elo 1,669, 5W/2D/1L (g1 W, g2 W, g3 W, g4 W, g5 D,
  g6 L, g7 W, g8 D), spare_plies 619, wall 922 s, mean think 2,680 ms,
  max 3,912 ms, 0 moves >= 10,000 ms. Full screening log in
  `~/workspace/makefun/trial0-v20b/TEST-RESULTS-v20.md`.
- vs v17 (Elo 1,598, 5W/1D/2L): +71 Elo. Gain g7 L->W (nodes-1M),
  regression g5 W->D. No stamp line: 4,096 + 5 B stamp would exceed the
  cap, so the file ships without one.

## Files

- `main.py` — the engine (4,096 bytes, ≤ 4,096).
- `LICENSE` — MIT, SPDX tag only.
- `.makefun/owner.json` — payout wallet.
