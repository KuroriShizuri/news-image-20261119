"""news-image-20261119 entry.

Copies the bundled front-page image (entry.png) to /output/entry.png.
Standard library only, no network access. The copy is byte-for-byte
identical on every run, so repeated runs write the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(SRC) != os.path.getsize(DST):
        raise RuntimeError("copy verification failed: size mismatch")


if __name__ == "__main__":
    main()
