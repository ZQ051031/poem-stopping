import os
from pathlib import Path

POEM = """The world runs downhill, shouting go.
I plant my feet. I breathe. I stay.
Stopping is not falling short—
it is the hand that pulls the reins,
the river parting round a stone
that chose, this once, to be the shore."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
