"""The Worst App Idea Ever Pitched.

Writes one sentence (<=240 chars) pitching the worst, most useless
app imaginable to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Only reads bundled code; writes only to the output directory.
"""
import os

LINE = (
    "Fernly is a $4.99-a-month app that sends urgent push alerts "
    "reminding you to water your plastic plants, then shows a "
    "wilting animation for the ones that cannot die."
)


def main():
    # Gate: the sealed scorer only accepts 1-240 chars of UTF-8 text,
    # one sentence, not only whitespace. Fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 240, len(LINE)
    # One sentence: ends with a period and no period is followed by
    # another sentence (the "." inside "$4.99" is not a sentence end).
    assert LINE.strip() == LINE and LINE.endswith(".")
    assert ". " not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
