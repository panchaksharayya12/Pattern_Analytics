import os
import sys
from pathlib import Path
import runpy

# Ensure root and src are in sys.path
ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR / "src"))
sys.path.insert(0, str(ROOT_DIR))

TARGET_APP = ROOT_DIR / "dashboard" / "app.py"

if TARGET_APP.exists():
    runpy.run_path(str(TARGET_APP), run_name="__main__")
else:
    raise FileNotFoundError(f"Dashboard app not found at: {TARGET_APP}")
