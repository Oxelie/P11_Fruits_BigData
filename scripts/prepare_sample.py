"""Build a small local sample of the fruits-360 dataset for pipeline development.

Copies a limited number of images from a subset of classes into data/sample,
preserving the class-per-folder structure expected by the PySpark pipeline
(the label is extracted from the parent folder name).
"""

import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = PROJECT_ROOT / "fruits" / "fruits-360_dataset" / "fruits-360" / "Training"
SAMPLE_DIR = PROJECT_ROOT / "data" / "sample"

N_CLASSES = 10
N_IMAGES_PER_CLASS = 30


def build_sample() -> None:
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"Dataset source not found: {SOURCE_DIR}")

    all_class_dirs = sorted(p for p in SOURCE_DIR.iterdir() if p.is_dir())
    step = max(len(all_class_dirs) // N_CLASSES, 1)
    class_dirs = all_class_dirs[::step][:N_CLASSES]

    if SAMPLE_DIR.exists():
        shutil.rmtree(SAMPLE_DIR)
    SAMPLE_DIR.mkdir(parents=True)

    total_copied = 0
    for class_dir in class_dirs:
        images = sorted(class_dir.glob("*.jpg"))[:N_IMAGES_PER_CLASS]
        dest_dir = SAMPLE_DIR / class_dir.name
        dest_dir.mkdir(parents=True, exist_ok=True)
        for image_path in images:
            shutil.copy2(image_path, dest_dir / image_path.name)
        total_copied += len(images)

    print(f"{len(class_dirs)} classes, {total_copied} images copied to {SAMPLE_DIR}")


if __name__ == "__main__":
    build_sample()
