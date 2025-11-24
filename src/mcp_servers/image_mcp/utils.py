import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 
STORAGE_DIR = BASE_DIR / "storage" / "images"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

def save_image_locally(img: bytes) -> str:
    file_name = f"{uuid.uuid4()}.jpg"
    file_path = STORAGE_DIR / file_name

    with open(file_path, "wb") as f:
        f.write(img)

    return str(file_path)

