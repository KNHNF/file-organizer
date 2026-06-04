# File Organizer

[![Python](https://img.shields.io/badge/Python-3.8+-3572A5?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-a78bfa?style=flat-square)](LICENSE)

Python CLI utility that automatically sorts files into category folders. Supports interactive mode, dry-run preview, undo, logging, and custom category configuration.

Useful for cleaning up cluttered directories like Downloads, project folders, or media collections.

---

## Features

| Feature | Description |
|---|---|
| Auto-sort | Moves files into category folders by extension |
| Dry-run | Preview what would happen without moving anything |
| Undo | Restore all files to their original locations |
| Custom config | Override default categories with `config.json` |
| Logging | All operations recorded in `organizer.log` |
| Interactive mode | Guided prompts for path and confirmation |

---

## Default Categories

| Category | Extensions |
|---|---|
| Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` |
| Documents | `.pdf` `.docx` `.doc` `.txt` `.xlsx` `.pptx` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` |
| Audio | `.mp3` `.wav` `.aac` `.flac` |
| Archives | `.zip` `.rar` `.7z` `.tar` `.gz` |
| Code | `.py` `.js` `.html` `.css` `.java` `.c` `.cpp` |
| Misc | anything that does not match a category |

---

## Usage

**Interactive mode (recommended)**

```bash
python src/organizer.py
```

Prompts for a folder path and asks for confirmation before moving anything.

**Direct mode**

```bash
python src/organizer.py "C:\Users\User\Downloads"
```

**Dry-run — preview only, nothing moves**

```bash
python src/organizer.py --dry "C:\Users\User\Downloads"
```

**Undo last sort**

```bash
python src/organizer.py --undo
```

Restores files using the auto-generated `undo_log.json`.

---

## Custom Categories

Create a `config.json` in the repo root to override defaults:

```json
{
    "images": [".jpg", ".png"],
    "documents": [".pdf", ".txt"],
    "music": [".mp3", ".wav"]
}
```

The script uses this file if present, otherwise falls back to built-in categories.

---

## Setup

```bash
git clone https://github.com/KNHNF/file-organizer.git
cd file-organizer

python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## Notes

- `undo_log.json` and `organizer.log` are auto-generated and excluded from version control
- Designed to be readable and extendable — suitable as a base for further automation work

---

## Author

**Karan Homayounfar** · MSc Data Science, UWE Bristol
[Portfolio](https://karan-portfolio-al7.pages.dev) · [LinkedIn](https://linkedin.com/in/karan-homayounfar) · [GitHub](https://github.com/KNHNF)

## License

MIT
