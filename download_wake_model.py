from pathlib import Path
import urllib.request
import zipfile
import shutil
import sys

ROOT = Path(__file__).resolve().parent
MODELS = ROOT / "models"
TARGET = MODELS / "vosk-model-small-en-us-0.15"
URL = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
ARCHIVE = MODELS / "vosk-wake-model.zip"

if TARGET.exists():
    print("Wake-word model already installed.")
    raise SystemExit(0)

MODELS.mkdir(parents=True, exist_ok=True)
print("Downloading the small offline English wake-word model (~40 MB)...")
try:
    urllib.request.urlretrieve(URL, ARCHIVE)
    with zipfile.ZipFile(ARCHIVE, "r") as zf:
        zf.extractall(MODELS)
    ARCHIVE.unlink(missing_ok=True)
    if not TARGET.exists():
        raise RuntimeError("The downloaded model folder was not found after extraction.")
    print("Offline ARGUS wake-word model installed.")
except Exception as exc:
    print("Wake-word model download failed:", exc)
    print("ARGUS will still offer SPACE as a manual activation fallback.")
    sys.exit(0)
