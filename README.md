[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/meviusorg5799/one-letter-for-your-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/meviusorg5799/one-letter-for-your-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

Entry for the [One Letter for Your Day bounty](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) on make.fun.

## The entry

Send exactly one letter, A to Z, standing for the word that describes your day. The judge compares letters two at a time and picks the one whose hidden word feels more vivid, funnier, or more true — so the whole game is choosing the right initial.

This entry picks its letter by drafting a shortlist of candidate words for a day, scoring each against the judge's own brief (vivid and specific first, then funny or surprising, then true to a real day, then a good fit between letter and word), and keeping the strongest. The winner is a concrete little scene from an ordinary day rather than a vague mood: something a reader can picture at once and repeat to a friend.

## How it works

`main.py` (Python 3.13, standard library only) reads the chosen letter from `entry.txt` beside it and writes it, plus a trailing newline, to `/output/entry.txt` — or to the directory named by `MAKEFUN_OUTPUT_DIR` when that is set. No clock, no network, no randomness: the same letter comes out every run.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
