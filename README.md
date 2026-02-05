# Simple Folder Organizer (Python)

A lightweight Python automation script that organizes files in a directory into categorized subfolders based on file type (Documents, Images, Videos, Audio, Archives, and more).

This project demonstrates practical file-system automation, safe scripting practices, and clean Python design suitable for real-world use and entry-level engineering roles.

---

## Features

- Automatically organizes files by extension
- Creates target folders if they don’t exist
- Skips important files to prevent accidental moves:
  - Python source files (`.py`)
  - README files
  - Folders
- Uses the script’s own location as the working directory (safe by default)
- Cross-platform (Windows, macOS, Linux)
- No third-party dependencies

---

## Why This Project

Manually organizing folders is a repetitive and error-prone task.

This script automates that process while prioritizing:
- **Safety** (never moves itself or folders)
- **Clarity** (easy-to-read logic)
- **Practical value** (usable in real environments)

The project is intentionally simple but structured to reflect how automation scripts are written and maintained in professional settings.

---

## Requirements

- Python **3.8 or newer**

No external libraries required — only Python’s standard library.

---

## How It Works

The script scans the folder where it lives and:
1. Identifies files by extension
2. Matches them to predefined categories
3. Moves them into corresponding folders
4. Sends unmatched files to an `Other/` folder

### File Categories

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`
- **Audio**: `.mp3`, `.wav`
- **Archives**: `.zip`, `.rar`, `.7z`

---

## Usage

1. Place `folder_organizer.py` inside the folder you want to organize
2. Open a terminal in that folder
3. Run:

```bash
python folder_organizer.py
## How to Use

1. Place `folder_organizer.py` inside the folder you want to organize
2. Open a terminal in that folder
3. Run one of the following commands:

### Preview changes (recommended first)
```bash
python folder_organizer.py --dry-run