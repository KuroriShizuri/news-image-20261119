# SPDX-License-Identifier: MIT
"""news-image-20261119 entry.

Copies the bundled front-page image (entry.png) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.png.
Python 3.13, standard library only, no network access. The copy is
byte-for-byte identical on every run, so repeated runs write the
same bytes. Before copying, the source is verified to be a JPEG or
PNG image of exactly 1024x1024 pixels, as the competition requires.
After copying, the destination is verified against the source by
size and SHA-256 digest.
"""

import hashlib
import os
import shutil
import struct

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


def _png_dimensions(f):
    """Read width/height from a PNG IHDR chunk (bytes 16..24)."""
    f.seek(16)
    width, height = struct.unpack(">II", f.read(8))
    return width, height


def _jpeg_dimensions(f):
    """Scan JPEG markers for the first SOF0/1/2 segment and read its size."""
    f.seek(2)
    while True:
        prefix = f.read(1)
        if prefix != b"\xff":
            raise RuntimeError("could not read JPEG dimensions: bad marker")
        code = f.read(1)
        if len(code) < 1:
            raise RuntimeError("could not read JPEG dimensions: truncated")
        code = code[0]
        if code in (0xC0, 0xC1, 0xC2):
            f.read(3)  # segment length (2) + precision (1)
            height, width = struct.unpack(">HH", f.read(4))
            return width, height
        if code == 0xD8 or code == 0x01 or 0xD0 <= code <= 0xD7:
            continue  # standalone markers carry no payload
        length = struct.unpack(">H", f.read(2))[0]
        f.seek(length - 2, 1)


def _validate_dimensions(path):
    """Require the source image to be exactly 1024x1024 pixels."""
    with open(path, "rb") as f:
        head = f.read(8)
        if head[:4] == b"\x89PNG":
            width, height = _png_dimensions(f)
        elif head[:3] == b"\xff\xd8\xff":
            width, height = _jpeg_dimensions(f)
        else:
            raise RuntimeError(
                "source image is neither PNG nor JPEG: %r" % head[:4]
            )
    if (width, height) != (1024, 1024):
        raise RuntimeError(
            "source image must be 1024x1024, got %dx%d" % (width, height)
        )


def main():
    _validate_magic(SRC)
    _validate_dimensions(SRC)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(SRC) != os.path.getsize(DST):
        raise RuntimeError("copy verification failed: size mismatch")
    if _sha256(SRC) != _sha256(DST):
        raise RuntimeError("copy verification failed: digest mismatch")
    print("copied %d bytes: %s -> %s" % (os.path.getsize(DST), SRC, DST))


if __name__ == "__main__":
    main()
