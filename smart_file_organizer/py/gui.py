import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import FileOrganizer
from history import UndoManager

class OrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.folder_path = tk.StringVar()

        self._build_ui()

    def _build_ui(self):
        # Folder select
        frame = tk.Frame(self.root, pady=10, padx=10)
        frame.pack()

        tk.Label(frame, text="Folder to organize:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame, textvariable=self.folder_path, width=50).grid(row=1, column=0, padx=5)
        tk.Button(frame, text="Browse", command=self.browse_folder).grid(row=1, column=1, padx=5)

        # Action buttons
        tk.Button(frame, text="Scan & Move", width=20, command=self.organize_files).grid(row=2, column=0, pady=10)
        tk.Button(frame, text="Undo Last Move", width=20, command=self.undo_last).grid(row=2, column=1, pady=10)

        # Message display
        self.message = tk.Label(frame, text="", fg="green")
        self.message.grid(row=3, column=0, columnspan=2)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def organize_files(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showwarning("Missing folder", "Please select a folder.")
            return

        try:
            organizer = FileOrganizer(folder)
            organizer.scan_files()
            if not organizer.files_by_extension:
                self.message.config(text="No files to organize.")
                return

            organizer.move_files()
            self.message.config(text="Files moved successfully!")
        except PermissionError:
            self.message.config(text="Permission denied to access the folder.", fg="red")
        except Exception as e:
            self.message.config(text=f"Error: {e}", fg="red")

    def undo_last(self):
        try:
            undo = UndoManager()
            undo.undo_last_move()
            self.message.config(text="Undo successful!")
        except FileNotFoundError:
            self.message.config(text="Original file no longer exists.", fg="red")
        except Exception as e:
            self.message.config(text=f"Undo failed: {e}", fg="red")

def launch_gui():
    root = tk.Tk()
    app = OrganizerApp(root)
    root.mainloop()
