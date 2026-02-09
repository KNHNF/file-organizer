Let’s tighten up your README and make the **undo workflow** crystal‑clear for anyone who downloads your project. You want users to understand:

- how to run the organizer  
- how to use interactive mode  
- how to undo a sort  
- what happens behind the scenes  

I’ll update your README accordingly and explain the undo flow in plain language.

---

# **📘 Updated README.md (with Interactive Mode + Undo Mode)**

You can paste this directly into your README.

```markdown
# 📂 File Organizer

A lightweight Python tool that automatically sorts files into categorized folders based on their type.  
Perfect for cleaning up cluttered directories like Downloads.

---

## ✨ Features

- Detects all files in a target folder  
- Sorts them into categories (Images, Documents, Videos, Audio, Archives, Code, Misc)  
- Creates category folders automatically  
- Moves files safely using `shutil`  
- **Interactive mode** (enter folder path + confirm action)  
- **Undo mode** (restore files to original locations)  
- Fully commented and beginner‑friendly code  

---

## 📁 Categories

The organizer currently supports:

- **Images** — `.jpg`, `.png`, `.jpeg`, `.gif`, `.bmp`, `.svg`  
- **Documents** — `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`  
- **Videos** — `.mp4`, `.mov`, `.avi`, `.mkv`  
- **Audio** — `.mp3`, `.wav`, `.aac`, `.flac`  
- **Archives** — `.zip`, `.rar`, `.7z`, `.tar`, `.gz`  
- **Code** — `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`  
- **Misc** — anything that doesn’t match a category  

---

## 🚀 How to Use

### **Option 1 — Interactive Mode (recommended)**

Just run the script with no arguments:

```bash
python src/organizer.py
```

You will be asked:

1. **Enter the folder path**  
2. The script checks if the folder exists  
3. You confirm with `y` or `n`  
4. Sorting begins  

Example:

```
📂 File Organizer — Interactive Mode

Enter the folder path to organize: C:\Users\User\Downloads
Folder found: C:\Users\User\Downloads
Are you sure you want to organize this folder? (y/n): y

➡️  photo.png → images/
➡️  resume.pdf → documents/
➡️  video.mp4 → videos/

📝 Undo log saved.
✅ Done! Files have been organized.
```

---

### **Option 2 — Direct Mode**

Run the script and pass a folder path:

```bash
python src/organizer.py "C:\Users\User\Downloads"
```

---

## ↩️ Undo Mode (Restore Files)

If you want to undo the last sort:

```bash
python src/organizer.py --undo
```

What happens:

- The script reads `undo_log.json`  
- Moves every file back to its original location  
- Deletes the undo log  
- Prints a summary  

Example:

```
↩️  Restored photo.png
↩️  Restored resume.pdf
↩️  Restored video.mp4

✅ Undo complete. Files restored.
```

If no undo log exists:

```
❌ No undo log found. Nothing to undo.
```

---

## 📦 Project Structure

```
file-organizer/
│
├── src/
│   └── organizer.py
│
├── examples/
│   └── (optional screenshots or sample folders)
│
├── README.md
└── .gitignore
```

---

## 🧭 Roadmap

- [x] Add interactive mode (ask for directory, confirm action)  
- [x] Add undo mode (restore files to original locations)  
- [ ] Add “dry run” mode (show what would happen)  
- [ ] Add config file for custom categories  
- [ ] Add logging to a file  
- [ ] Add GUI version (Tkinter)  
- [ ] Add progress bar  
- [ ] Add optional `.exe` build for Windows users  

---

# **🟦 How Undo Works **

When the script organizes files, it creates a file called:

```
undo_log.json
```

This file stores:

- the original location of each file  
- the new location after sorting  

Example:

```json
{
    "C:/Users/User/Downloads/photo.png": "C:/Users/User/Downloads/images/photo.png"
}
```

When the user runs:

```
python src/organizer.py --undo
```

The script:

1. Reads `undo_log.json`  
2. Moves each file back to its original path  
3. Deletes the undo log  
4. Prints a summary  

This means:

- The user **does NOT** run the script again normally  
- They run it **with the `--undo` flag**  
- Undo works only for the **most recent sort**  

---
