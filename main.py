"""news-image-20261119 entry.

Copies the bundled front-page image (entry.png) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.png.
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
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUTPUT_DIR, "entry.png")


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _validate_magic(path):
    """Check the source image starts with a JPEG or PNG magic number."""
    with open(path, "rb") as f:
        magic = f.read(4)
    if magic[:3] == b"\xff\xd8\xff" or magic == b"\x89PNG":
        return
    raise RuntimeError(
        "source image has unrecognised magic bytes: %r" % magic
    )


def main():
    _validate_magic(SRC)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(SRC) != os.path.getsize(DST):
        raise RuntimeError("copy verification failed: size mismatch")
    if _sha256(SRC) != _sha256(DST):
        raise RuntimeError("copy verification failed: digest mismatch")
    print("copied %d bytes: %s -> %s" % (os.path.getsize(DST), SRC, DST))


if __name__ == "__main__":
    main()
