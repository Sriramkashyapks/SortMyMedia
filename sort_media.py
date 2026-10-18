from pathlib import Path
import shutil

# Ask for the root folder path
folder_path = input("Enter the root folder path: ").strip().strip('"')
ROOT_FOLDER = Path(folder_path).expanduser().resolve()

# Validate the folder
if not ROOT_FOLDER.is_dir():
    print("Invalid folder path. Please check the path and try again.")
    exit()

# Create destination folders
PHOTO_FOLDER = ROOT_FOLDER / "Photos"
VIDEO_FOLDER = ROOT_FOLDER / "Videos"

PHOTO_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".heic", ".heif",
    ".webp", ".gif", ".bmp", ".tiff", ".tif",
    ".raw", ".dng", ".cr2", ".nef", ".arw"
}

VIDEO_EXTENSIONS = {
    ".mp4", ".mov", ".mkv", ".avi", ".wmv",
    ".flv", ".webm", ".m4v", ".3gp", ".mts",
    ".m2ts", ".mpg", ".mpeg", ".vob"
}


def get_unique_path(destination):
    """Generate a unique filename to avoid overwriting."""
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_destination = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_media():
    PHOTO_FOLDER.mkdir(exist_ok=True)
    VIDEO_FOLDER.mkdir(exist_ok=True)

    photo_count = 0
    video_count = 0

    # Get all files before moving anything
    all_files = list(ROOT_FOLDER.rglob("*"))

    for file_path in all_files:

        if not file_path.is_file():
            continue

        # Skip files already inside Photos or Videos
        if PHOTO_FOLDER in file_path.parents:
            continue

        if VIDEO_FOLDER in file_path.parents:
            continue

        extension = file_path.suffix.lower()

        if extension in PHOTO_EXTENSIONS:
            destination = get_unique_path(
                PHOTO_FOLDER / file_path.name
            )

            shutil.move(str(file_path), str(destination))
            photo_count += 1

        elif extension in VIDEO_EXTENSIONS:
            destination = get_unique_path(
                VIDEO_FOLDER / file_path.name
            )

            shutil.move(str(file_path), str(destination))
            video_count += 1

    print("\nMedia organization completed!")
    print(f"Photos moved: {photo_count}")
    print(f"Videos moved: {video_count}")
    print(f"Photos folder: {PHOTO_FOLDER}")
    print(f"Videos folder: {VIDEO_FOLDER}")


if __name__ == "__main__":
    organize_media()