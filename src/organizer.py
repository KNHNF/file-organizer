from pathlib import Path
import json
import shutil
import time
import sys

# Configuration

DEFAULT_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".aac", ".flac"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
}

CONFIG_FILE = "config.json"
UNDO_LOG = "undo_log.json"
LOG_FILE = "organizer.log"


# Helpers

def load_categories():
    """Load categories from config.json if present."""
    if Path(CONFIG_FILE).exists():
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_CATEGORIES


CATEGORIES = load_categories()


def log(message):
    """Append a message to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def get_category(extension):
    """Return category name for a file extension."""
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "misc"


def save_undo_log(moves):
    """Save original → new file paths to undo_log.json."""
    with open(UNDO_LOG, "w") as f:
        json.dump(moves, f, indent=4)


# Undo last sort

def undo_last_sort():
    """Restore files using undo_log.json."""
    if not Path(UNDO_LOG).exists():
        print("No undo log found.")
        return

    with open(UNDO_LOG, "r") as f:
        moves = json.load(f)

    print("Undoing last sort...\n")

    for original, new in moves.items():
        original_path = Path(original)
        new_path = Path(new)

        if new_path.exists():
            original_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(new_path), str(original_path))
            print(f"Restored {new_path.name}")
            log(f"Restored {new_path} -> {original_path}")

    Path(UNDO_LOG).unlink()
    print("Undo complete.")
    log("Undo completed")


# Dry run

def dry_run(folder_path):
    """Preview sorting actions without moving files."""
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist.")
        return

    print("Dry run (no files moved):\n")

    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix
            category = get_category(ext)
            print(f"{item.name} → {category}/")

    print("\nPreview complete.")


# Progress bar

def progress_bar(current, total):
    """Display a simple progress bar."""
    percent = int((current / total) * 100)
    bar = "#" * (percent // 5)
    print(f"[{bar:<20}] {percent}%", end="\r")


# Main sorting function

def organize_folder(folder_path):
    """Sort files into category folders and save undo log."""
    folder = Path(folder_path)

    if not folder.exists():
        print(f"Folder does not exist: {folder}")
        return

    print(f"Organizing: {folder.resolve()}\n")

    moves = {}
    files = [f for f in folder.iterdir() if f.is_file()]
    total = len(files)

    for i, item in enumerate(files, start=1):
        ext = item.suffix
        category = get_category(ext)

        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)

        new_path = target_dir / item.name
        moves[str(item)] = str(new_path)

        shutil.move(str(item), str(new_path))
        print(f"{item.name} → {category}/")
        log(f"Moved {item} -> {new_path}")

        progress_bar(i, total)
        time.sleep(0.02)

    save_undo_log(moves)
    print("\nUndo log saved.")
    print("Done. Files have been organized.")
    log("Sort completed")


# CLI entry point

def interactive_mode():
    """Ask the user for a folder path and confirmation."""
    print("File Organizer\n")

    folder_path = input("Enter the folder path to organize: ").strip()
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder not found.")
        return

    print(f"Folder found: {folder.resolve()}")
    confirm = input("Proceed with organizing? (y/n): ").lower()

    if confirm == "y":
        organize_folder(folder_path)
    else:
        print("Operation cancelled.")


if __name__ == "__main__":

    if "--undo" in sys.argv:
        undo_last_sort()
        sys.exit()

    if "--dry" in sys.argv:
        if len(sys.argv) < 3:
            print("Usage: python organizer.py --dry <folder_path>")
            sys.exit()
        dry_run(sys.argv[2])
        sys.exit()

    if len(sys.argv) == 1:
        interactive_mode()
        sys.exit()

    organize_folder(sys.argv[1])
