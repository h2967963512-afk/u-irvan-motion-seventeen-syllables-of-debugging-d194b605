"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is a haiku about debugging in 5-7-5 (17 syllables):
# a cursor blinking at 3am, a log that insists nothing is wrong, and
# a last line that reframes the first two — the code still lies.
# Syllables: cursor(2) blinks(1) at(1) three(1) = 5; the(1) log(1)
# insists(2) nothing's(2) wrong(1) = 7; but(1) the(1) code(1)
# still(1) lies(1) = 5. Total 17, 77 characters — inside the cap.
import os

TEXT = (
    "cursor blinks at three\n"
    "the log insists nothing's wrong\n"
    "but the code still lies"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
