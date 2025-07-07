# Smart-File-Organizer

Automatically sort files in a folder into subfolders based on file extensions.

---

## Features

- Scan a folder and classify files by extension (e.g., `.jpg`, `.pdf`, `.py`).
- Create destination subfolders and move files accordingly.
- Log all moved files with source, destination, and timestamps.
- Undo the last move operation.
- User-friendly GUI built with Tkinter.
- Console mode available for quick use.
- Handles errors like permission issues and naming conflicts gracefully.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-file-organizer.git
   cd smart-file-organizer

---
## Usage

1. Run Console Mode    
python3 main.py
2. Choose console mode:
Run [c]onsole or [g]ui? c
3. Follow the prompts:
Enter the path to the folder you want to organize: /Users/you/Downloads
Choose action: [m]ove, [u]ndo last move, [q]uit: m

GUI Mode
1. Run the script:
python3 main.py
2. Choose console mode:
Run [c]onsole or [g]ui? g

GUI features:
Browse: Choose the folder to organize
Scan & Move: Automatically sort files by type
Undo Last Move: Reverts the most recent organization
Real-time messages and feedback in the interface

## Screenshots

### GUI Main Window

![GUI Example](screenshots/gui.png)