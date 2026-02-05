import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}

def organize_files(target_folder: str, dry_run: bool = False):
    script_name = os.path.basename(__file__)

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Skip folders and the script itself
        if os.path.isdir(file_path) or filename == script_name:
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        destination = "Other"

        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                destination = folder
                break

        target_dir = os.path.join(target_folder, destination)

        if dry_run:
            print(f"[DRY-RUN] Would move '{filename}' → '{destination}/'")
        else:
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved '{filename}' → '{destination}/'")

    if dry_run:
        print("\nDry-run complete. No files were moved.")
    else:
        print("\n✅ Folder organized successfully!")

def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by file type."
    )
    parser.add_argument(
        "--path",
        type=str,
        default=os.path.dirname(os.path.abspath(__file__)),
        help="Target folder to organize (default: script location)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files",
    )

    args = parser.parse_args()

    organize_files(args.path, args.dry_run)

if __name__ == "__main__":
    main()
