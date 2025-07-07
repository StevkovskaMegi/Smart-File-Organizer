import os
import shutil
from collections import defaultdict
from smart_file_organizer.logger import MoveLogger


class FileOrganizer:
    def __init__(self, folder_path: str):
        self.folder_path = os.path.abspath(folder_path)
        self.files_by_extension = defaultdict(list)
        self.logger = MoveLogger()


        if not os.path.isdir(self.folder_path):
            raise ValueError(f"{self.folder_path} is not a valid directory.")

    def scan_files(self):
        self.files_by_extension.clear()
        for entry in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path, entry)
            if os.path.isfile(full_path):
                _, ext = os.path.splitext(entry)
                ext = ext.lower().strip('.')
                if ext:
                    self.files_by_extension[ext].append(full_path)

    def move_files(self):
        """
        Move files into subfolders by extension.
        """
        for ext, files in self.files_by_extension.items():
            dest_folder = os.path.join(self.folder_path, ext)
            os.makedirs(dest_folder, exist_ok=True)

            for src_path in files:
                file_name = os.path.basename(src_path)
                dest_path = os.path.join(dest_folder, file_name)

                # Handle naming conflicts
                counter = 1
                while os.path.exists(dest_path):
                    name, extn = os.path.splitext(file_name)
                    dest_path = os.path.join(dest_folder, f"{name}_{counter}{extn}")
                    counter += 1

                try:
                    shutil.move(src_path, dest_path)
                    self.logger.log_move(src_path, dest_path)
                    print(f"Moved: {src_path} → {dest_path}")
                except Exception as e:
                    print(f"Failed to move {src_path}: {e}")

    def print_summary(self):
        if not self.files_by_extension:
            print("No files found.")
            return

        print("Files grouped by extension:")
        for ext, files in self.files_by_extension.items():
            print(f".{ext}: {len(files)} file(s)")
