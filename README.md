# 📂 File Organizer

A lightweight and beginner‑friendly Python tool that automatically sorts files into categorized folders based on their type.  
Perfect for cleaning up cluttered directories like Downloads, project folders, or media dumps.

The tool includes interactive mode, dry‑run preview, undo support, logging, config file customization, and Windows‑safe output handling.

---

## ✨ Features

- Automatically sorts files into category folders  
- Interactive mode for beginners  
- Dry‑run mode (preview actions without moving files)  
- Undo mode (restore files to original locations)  
- Config file support (`config.json`) for custom categories  
- Logging to `organizer.log`  
- Windows CMD‑safe printing (no Unicode crashes)  
- Simple progress bar  
- GUI mode placeholder for future expansion  
- Fully commented and easy to understand  

---

## 📁 Default Categories

The tool sorts files into these folders:

- **Images** — `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`  
- **Documents** — `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`  
- **Videos** — `.mp4`, `.mov`, `.avi`, `.mkv`  
- **Audio** — `.mp3`, `.wav`, `.aac`, `.flac`  
- **Archives** — `.zip`, `.rar`, `.7z`, `.tar`, `.gz`  
- **Code** — `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`  
- **Misc** — anything that doesn’t match a category  

You can override these by creating a `config.json` (explained below).

---

## 🚀 How to Use

### **1. Clone the repository**

```bash
git clone https://github.com/<your-username>/file-organizer.git
cd file-organizer
```

---

## **2. Run the script**

### **Option A — Interactive Mode (recommended)**  

Just run:

```bash
python src/organizer.py
```

You will be asked:

1. Enter folder path  
2. Confirm the action  
3. Sorting begins  

---

### **Option B — Direct Mode**

```bash
python src/organizer.py "C:\Users\User\Downloads"
```

---

### **Option C — Dry‑Run Mode (preview only)**

```bash
python src/organizer.py --dry "C:\Users\User\Downloads"
```

This shows what *would* happen without moving any files.

---

### **Option D — Undo Last Sort**

If something went wrong or you want to revert:

```bash
python src/organizer.py --undo
```

This restores all files using `undo_log.json`.

---

### **Option E — GUI Mode (placeholder)**

```bash
python src/organizer.py --gui
```

A Tkinter GUI will be added in a future update.

---

## ⚙️ Custom Categories (config.json)

You can create a `config.json` in the project folder to override categories:

```json
{
    "images": [".jpg", ".png"],
    "documents": [".pdf", ".txt"],
    "music": [".mp3", ".wav"]
}
```

The script will automatically load this file instead of the defaults.

---

## 📝 Logging

All actions (moves, restores, errors) are recorded in:

```
organizer.log
```

Logging is UTF‑8 safe and will never crash on Windows.

---

## 🛡 Windows CMD Compatibility

Windows CMD cannot display emojis or arrows.  
To prevent crashes, the script uses:

- `safe_print()`  
- `safe_print_inline()`  
- ASCII‑safe logging  

This ensures the tool works on:

- CMD  
- PowerShell  
- Windows Terminal  
- VS Code terminal  
- PyInstaller EXE  

---

## 📦 Project Structure

```
file-organizer/
│
├── src/
│   └── organizer.py
│
├── config.json        (optional)
├── undo_log.json      (auto-generated)
├── organizer.log      (auto-generated)
└── README.md
```
