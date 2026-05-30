# File Organizer

A lightweight Python utility that automatically sorts files into category‑based folders.  
Useful for cleaning up cluttered directories such as Downloads, project folders, or media collections.  
The tool supports interactive mode, dry‑run preview, undo functionality, logging, and optional category customization.

---

## Features

- Automatically sorts files into category folders  
- Interactive mode for guided usage  
- Dry‑run mode to preview actions without moving files  
- Undo mode to restore files to their original locations  
- Optional `config.json` for custom category definitions  
- Logging of all file operations  
- Simple progress bar  
- Clean, readable code suitable for beginners  

---

## Default Categories

Files are sorted into the following groups:

- Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`  
- Documents: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`  
- Videos: `.mp4`, `.mov`, `.avi`, `.mkv`  
- Audio: `.mp3`, `.wav`, `.aac`, `.flac`  
- Archives: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`  
- Code: `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`  
- Misc: any file that does not match a category  

You can override these by creating a `config.json`.

---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/file-organizer.git
cd file-organizer
```

---

### 2. Run the script

#### Interactive mode (recommended)

```bash
python src/organizer.py
```

You will be prompted for a folder path and confirmation before sorting begins.

---

#### Direct mode

```bash
python src/organizer.py "C:\Users\User\Downloads"
```

---

#### Dry‑run mode (preview only)

```bash
python src/organizer.py --dry "C:\Users\User\Downloads"
```

This shows what would happen without moving any files.

---

#### Undo last sort

```bash
python src/organizer.py --undo
```

This restores files using the automatically generated `undo_log.json`.

---

## Custom Categories (config.json)

You can define your own categories by creating a `config.json` file:

```json
{
    "images": [".jpg", ".png"],
    "documents": [".pdf", ".txt"],
    "music": [".mp3", ".wav"]
}
```

If present, the script will use this file instead of the default categories.

---

## Logging

All file operations are recorded in `organizer.log`.  
This includes moves, restores, and any errors encountered during execution.

---

## Notes

- `undo_log.json` and `organizer.log` are generated automatically and should not be committed to version control.  
- The script is designed to be simple and readable, making it suitable for beginners or as a base for further expansion.  
- A GUI version may be added in a future update.
