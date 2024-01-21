import os
import shutil
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python sync_previous_module.py <source_dir_name> <dest_dir_name>")
        sys.exit(1)

    base_path = "/Users/mainframe/PycharmProjects/minitorch"
    current_dir = "minitorch-module-1-RyanLisse"
    files_to_sync_path = os.path.join(base_path, current_dir, "files_to_sync.txt")

    try:
        with open(files_to_sync_path, "r") as f:
            files_to_move = f.read().splitlines()
    except FileNotFoundError:
        print(
            f"Error: 'files_to_sync.txt' not found in {os.path.join(base_path, current_dir)}"
        )
        sys.exit(1)

    source_dir_name = sys.argv[1]  # e.g., 'minitorch-module-0-RyanLisse'
    dest_dir_name = sys.argv[2]  # e.g., 'minitorch-module-1-RyanLisse'
    source = os.path.join(base_path, source_dir_name)
    dest = os.path.join(base_path, dest_dir_name)

    if not os.path.isdir(source):
        print(f"Error: Source directory '{source}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(dest):
        print(f"Error: Destination directory '{dest}' does not exist.")
        sys.exit(1)

    for file in files_to_move:
        source_file = os.path.join(source, file)
        dest_file = os.path.join(dest, file)

        if not os.path.isfile(source_file):
            print(f"Warning: '{source_file}' does not exist and will not be copied.")
            continue

        try:
            shutil.copy(source_file, dest_file)
            print(f"Copied '{source_file}' to '{dest_file}'")
        except Exception as e:
            print(f"Error copying '{source_file}': {e}")

    print(f"Finished synchronizing files.")


if __name__ == "__main__":
    main()
