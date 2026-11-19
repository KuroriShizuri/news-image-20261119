"""news-image-20261119 entry.

Copies the bundled front-page image (entry.png) to /output/entry.png.
Python 3.13, standard library only, no network access. The copy is
byte-for-byte identical on every run, so repeated runs write the
same bytes. After copying, the destination is verified against the
source by size and SHA-256 digest.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"  # the sandbox output directory make.fun reads


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(SRC) != os.path.getsize(DST):
        raise RuntimeError("copy verification failed: size mismatch")
    if _sha256(SRC) != _sha256(DST):
        raise RuntimeError("copy verification failed: digest mismatch")


if __name__ == "__main__":
    main()
