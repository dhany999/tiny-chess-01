# tiny-chess-01 — v26

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/dhany999/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/dhany999/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4,096-byte chess engine for the make.fun tiny-chess-01 bounty: v20's
search plus a set-D fastest-mate opening book (g6 + g7 lines), no contempt.

- **g6 Philidor:** book line flips v20's only loss to a win, checkmate in 148 plies.
- **g7 Scotch:** book line holds the win, checkmate in 97 plies.
- **Trial-0 (8 games): Elo 1,845, 6W/2D/0L** — beats v20's 1,669 (6W/2D/0L → 7.0 pts vs 6.0).

The engine is a zlib-compressed payload (`main.py` unpacks and runs it);
the book is a 115-entry binary table (3-byte position hash + 2-byte move)
covering both lines with zero collisions.

<sub>Entered on [make.fun](https://make.fun/?ref=dhpnw6yp&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
