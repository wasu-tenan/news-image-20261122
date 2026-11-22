"""news-image-20261122 entrypoint (Python 3.13, standard library only).

Copies the committed entry.png beside this file to the output directory
(MAKEFUN_OUTPUT_DIR, default /output). Deterministic: the same bytes
every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Resolve the source image next to this script itself, never relative
# to the caller's current working directory.
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The output directory may not exist yet on a fresh grader run, so
# create it (including any missing parents) before copying into it.
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, OUT / "entry.png")
