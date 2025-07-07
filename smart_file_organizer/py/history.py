import os
import json
import shutil
from datetime import datetime

class UndoManager:
    def __init__(self, history_file='history.json'):
        self.history_file = history_file
        self.history = self._load_history()

    def _load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return []

    def save_move(self, source: str, destination: str):
        self.history.append({
            "source": source,
            "destination": destination,
            "timestamp": datetime.now().isoformat()
        })
        self._save()

    def _save(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def undo_last_move(self):
        if not self.history:
            print("Nothing to undo.")
            return

        last_move = self.history.pop()
        src = last_move["destination"]
        dst = last_move["source"]

        # Handle name conflicts
        counter = 1
        original_name = os.path.basename(dst)
        while os.path.exists(dst):
            name, ext = os.path.splitext(original_name)
            dst = os.path.join(os.path.dirname(dst), f"{name}_undo{counter}{ext}")
            counter += 1

        try:
            shutil.move(src, dst)
            print(f"Undo successful: {src} → {dst}")
        except FileNotFoundError:
            print(f"File not found: {src}")
            self.history.append(last_move)  # Keep it in history
        except PermissionError:
            print(f"Permission denied: {src}")
            self.history.append(last_move)
        except Exception as e:
            print(f"Undo failed: {e}")
            self.history.append(last_move)
        finally:
            self._save()
            