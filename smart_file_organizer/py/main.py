from organizer import FileOrganizer
from history import UndoManager
from gui import launch_gui

def main():
    folder = input("Enter the path to the folder you want to organize: ")
    try:
        organizer = FileOrganizer(folder)
        organizer.scan_files()
        organizer.print_summary()

        action = input("Choose action: [m]ove, [u]ndo last move, [q]uit: ").lower()
        if action == 'm':
            organizer.move_files()
        elif action == 'u':
            UndoManager().undo_last_move()
        else:
            print("Exiting.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    choice = input("Run [c]onsole or [g]ui? ").lower()
    if choice == 'g':
        launch_gui()
    else:
        # existing console logic
        folder = input("Enter the path to the folder you want to organize: ")
        try:
            organizer = FileOrganizer(folder)
            organizer.scan_files()
            organizer.print_summary()

            action = input("Choose action: [m]ove, [u]ndo last move, [q]uit: ").lower()
            if action == 'm':
                organizer.move_files()
            elif action == 'u':
                UndoManager().undo_last_move()
            else:
                print("Exiting.")
        except Exception as e:
            print(f"Error: {e}")
