import os
import shutil
import sys
from pathlib import Path

# -----------------------------
# File categories
# -----------------------------
CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".aac", ".flac"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
}

# -----------------------------
# Helper: get category for file
# -----------------------------


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "misc"


# -----------------------------
# Main organizer function
# -----------------------------
def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print(f"❌ Folder does not exist: {folder}")
        return

    print(f"📁 Organizing: {folder.resolve()}")

    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix
            category = get_category(ext)

            target_dir = folder / category
            target_dir.mkdir(exist_ok=True)

            shutil.move(str(item), str(target_dir / item.name))
            print(f"➡️  {item.name} → {category}/")

    print("\n✅ Done! Files have been organized.")


# -----------------------------
# CLI entry point
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path>")
        sys.exit(1)

    organize_folder(sys.argv[1])
