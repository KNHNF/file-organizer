from pathlib import Path
import time
import json
import os
import shutil
import sys

# ---------------------------------------------------
# Safe print functions for Windows CMD compatibility
# CMD cannot display emojis or arrows, so these
# wrappers prevent crashes by stripping unsupported
# characters when needed.
# ---------------------------------------------------


def safe_print(text):
    """Print normally, but fall back to ASCII if Unicode fails."""
    try:
        print(text)
    except UnicodeEncodeError:
        ascii_text = text.encode("ascii", "ignore").decode()
        print(ascii_text)


def safe_print_inline(text):
    """Same as safe_print(), but keeps the cursor on the same line."""
    try:
        print(text, end="")
    except UnicodeEncodeError:
        ascii_text = text.encode("ascii", "ignore").decode()
        print(ascii_text, end="")

# ---------------------------------------------------
# Category system
# Default file categories used when no config.json is present.
# Users can override these by creating their own config.json file.
# If config.json exists, categories are loaded from it.
# Otherwise, the default categories below are used.
# This allows users to customize how files are sorted.

# ---------------------------------------------------


DEFAULT_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".aac", ".flac"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
}

CONFIG_FILE = "config.json"      # Optional user-defined categories
UNDO_LOG = "undo_log.json"       # Stores original file locations
LOG_FILE = "organizer.log"       # Log file for actions

# ---------------------------------------------------
# Load categories from config.json if available
# ---------------------------------------------------


def load_categories():
    """Load custom categories if config.json exists."""
    if Path(CONFIG_FILE).exists():
        with open(CONFIG_FILE, "r") as f:
            safe_print("⚙️  Loaded categories from config.json")
            return json.load(f)
    return DEFAULT_CATEGORIES


CATEGORIES = load_categories()

# ---------------------------------------------------
# Logging helper (UTF‑8 safe)
# Ensures logs never crash due to Unicode characters.
# ---------------------------------------------------


def log(message):
    """Write logs safely without Unicode errors."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except UnicodeEncodeError:
        ascii_text = message.encode("ascii", "ignore").decode()
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(ascii_text + "\n")

# ---------------------------------------------------
# Determine category for a file based on extension
# ---------------------------------------------------


def get_category(extension):
    """Return the category name for a given file extension."""
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "misc"

# ---------------------------------------------------
# Save undo information so the user can restore files
# ---------------------------------------------------


def save_undo_log(moves):
    """Save original → new file paths to undo_log.json."""
    with open(UNDO_LOG, "w") as f:
        json.dump(moves, f, indent=4)

# ---------------------------------------------------
# undo_log.json stores original file paths so the user can restore files later.
# ---------------------------------------------------


def undo_last_sort():
    """Restore files using undo_log.json."""
    if not Path(UNDO_LOG).exists():
        safe_print("❌ No undo log found. Nothing to undo.")
        return

    with open(UNDO_LOG, "r") as f:
        moves = json.load(f)

    safe_print("↩️  Undoing last sort...\n")

    for original, new in moves.items():
        original_path = Path(original)
        new_path = Path(new)

        if new_path.exists():
            original_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(new_path), str(original_path))
            safe_print(f"↩️  Restored {new_path.name}")
            log(f"Restored {new_path} -> {original_path}")

    Path(UNDO_LOG).unlink()
    safe_print("\n✅ Undo complete. Files restored.")
    log("Undo completed")

# ---------------------------------------------------
# Dry-run mode: shows what WOULD happen
# ---------------------------------------------------


def dry_run(folder_path):
    """Preview sorting actions without moving any files."""
    folder = Path(folder_path)

    if not folder.exists():
        safe_print("❌ Folder does not exist.")
        return

    safe_print("🔍 Dry Run — No files will be moved\n")

    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix
            category = get_category(ext)
            safe_print(f"➡️  {item.name} → {category}/")

    safe_print("\nℹ️  This was only a preview. No changes were made.")

# ---------------------------------------------------
# Simple text-based progress bar
# ---------------------------------------------------


def progress_bar(current, total):
    """Display a progress bar during sorting."""
    percent = int((current / total) * 100)
    bar = "#" * (percent // 5)
    safe_print_inline(f"[{bar:<20}] {percent}%\r")

# ---------------------------------------------------
# Main sorting function
# ---------------------------------------------------


def organize_folder(folder_path):
    """Sort files into category folders and save undo log."""
    folder = Path(folder_path)

    if not folder.exists():
        safe_print(f"❌ Folder does not exist: {folder}")
        return

    safe_print(f"📁 Organizing: {folder.resolve()}\n")

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
        safe_print(f"➡️  {item.name} → {category}/")
        log(f"Moved {item} -> {new_path}")

        progress_bar(i, total)
        time.sleep(0.05)

    save_undo_log(moves)
    safe_print("\n\n📝 Undo log saved.")
    safe_print("✅ Done! Files have been organized.")
    log("Sort completed")

# ---------------------------------------------------
# Interactive mode:
# Asks for a folder path and confirmation before sorting.
# ---------------------------------------------------


def interactive_mode():
    """Ask the user for a folder path and confirmation."""
    safe_print("📂 File Organizer — Interactive Mode\n")

    folder_path = input("Enter the folder path to organize: ").strip()
    folder = Path(folder_path)

    if not folder.exists():
        safe_print("❌ Folder not found.")
        return

    safe_print(f"Folder found: {folder.resolve()}")
    confirm = input(
        "Are you sure you want to organize this folder? (y/n): ").lower()

    if confirm == "y":
        organize_folder(folder_path)
    else:
        safe_print("❌ Operation cancelled.")

# ---------------------------------------------------
# GUI placeholder (future feature)
# ---------------------------------------------------


def gui_mode():
    """Placeholder for future Tkinter GUI."""
    safe_print("🖥️ GUI mode is planned but not implemented yet.")
    safe_print("This will use Tkinter in a future update.")

# ---------------------------------------------------
# CLI entry point
# Command-line interface:
# - No arguments → interactive mode
#  --dry <path> → preview actions
#  --undo → restore last sort
#  --gui → placeholder for future GUI
#  <path> → direct mode
# ---------------------------------------------------


if __name__ == "__main__":

    # Undo mode
    if "--undo" in sys.argv:
        undo_last_sort()
        sys.exit()

    # Dry run mode
    if "--dry" in sys.argv:
        if len(sys.argv) < 3:
            safe_print("Usage: python organizer.py --dry <folder_path>")
            sys.exit()
        dry_run(sys.argv[2])
        sys.exit()

    # GUI mode
    if "--gui" in sys.argv:
        gui_mode()
        sys.exit()

    # Interactive mode (default)
    if len(sys.argv) == 1:
        interactive_mode()
        sys.exit()

    # Direct mode
    organize_folder(sys.argv[1])
