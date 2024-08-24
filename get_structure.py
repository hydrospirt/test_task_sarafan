import fnmatch
import os
from pathlib import Path

EXCLUDE_DIRS = ["__pycache__", "venv", ".git",
                ".idea", "*.egg-info", "migrations"]
EXCLUDE_FILES = ["*.pyc", "*.pyo", "*.png",
                 "*.jpg", "*.jpeg", "*.gif",
                 "*.bmp", "*.svg"]


def should_exclude(item):
    if item in EXCLUDE_DIRS:
        return True
    if any(fnmatch.fnmatch(item, pattern) for pattern in EXCLUDE_FILES):
        return True
    return False


def print_directory_structure(root_dir, indent=""):
    try:
        items = os.listdir(root_dir)
    except PermissionError:
        return

    items.sort()

    for item in items:
        item_path = os.path.join(root_dir, item)
        if should_exclude(item):
            continue

        if os.path.isdir(item_path):
            print(f"{indent}├──{item}/")
            print_directory_structure(item_path, indent + "│   ")
        else:
            print(f"{indent}├──{item}")


BASE_DIR = Path(__file__).resolve().parent
root_directory = BASE_DIR
print_directory_structure(root_directory)
