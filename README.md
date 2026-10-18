# SortMyMedia

A simple Python script that automatically organizes photos and videos from a root folder into separate folders based on file type. Supports nested folders and prevents accidental file overwrites.

## 1. What is this for?

SortMyMedia is a Python utility designed to organize photos and videos scattered across a folder and its subfolders.

Instead of manually searching for media files and moving them one by one, you can provide a root folder path and let the script automatically classify and organize your media.

This is useful when:
- Transferring photos and videos from a phone or camera to a computer.
- Organizing large collections of media files.
- Cleaning up folders containing a mixture of photos, videos, and other files.

## 2. What this will do

When you run the script, it will:

1. Ask you to enter the path of the root folder you want to organize.
2. Create two subfolders inside the specified root folder:
   - `Photos`
   - `Videos`
3. Scan the root folder and its existing subfolders for supported media files.
4. Identify photos and videos based on their file extensions.
5. Move photos into the `Photos` folder.
6. Move videos into the `Videos` folder.
7. Leave unsupported file types and other files untouched.
8. Avoid overwriting files when duplicate filenames exist by generating a unique filename.

### Example

Before running the script:

```text
MyMedia/
├── IMG_001.jpg
├── VID_001.mp4
├── Documents/
│   ├── IMG_002.png
│   └── VID_002.mov
└── Notes.txt
```

After running the script:

```text
MyMedia/
├── Photos/
│   ├── IMG_001.jpg
│   └── IMG_002.png
├── Videos/
│   ├── VID_001.mp4
│   └── VID_002.mov
├── Documents/
└── Notes.txt
```

The original media files are moved into the destination folders. They are not copied, so the files will no longer remain in their original locations.

## 3. What is required before running the script?

### Prerequisites

- **Python 3:** Python must be installed on your computer. Python 3.9 or newer is recommended.
- **Operating system:** macOS, Windows, or Linux.
- **Terminal access:** Terminal on macOS/Linux or Command Prompt/PowerShell on Windows.
- **Folder access:** You must have permission to read and move files in the folder you want to organize.
- **Media files:** The root folder should contain photos or videos that you want to sort.

### Python installation

Check whether Python is already installed by running:

```bash
python3 --version
```

If a Python version is displayed, you can proceed.

If Python is not installed, download it from:

https://www.python.org/downloads/

On Windows, you may need to use `python` instead of `python3` in the commands below.

### Important things to know

- Back up important files before running the script.
- The script moves files rather than copying them.
- Only file extensions included in the script's supported photo and video lists are classified.
- Files already inside the `Photos` and `Videos` destination folders are skipped.
- Files with unsupported extensions are not moved.
- Duplicate filenames are handled by adding a number to the new filename, such as `IMG_001_1.jpg`.

## 4. How to run this

### Step 1: Download or clone the repository

Clone the repository using Git:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of this repository.

Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Open the project folder

Navigate to the folder containing the Python script.

For example:

```bash
cd SortMyMedia
```

### Step 3: Run the script

Execute the following command:

```bash
python3 media_sort.py
```

If your script has a different filename, replace `media_sort.py` with that filename.

### Step 4: Enter the root folder path

The script will prompt:

```text
Enter the root folder path:
```

Enter the folder you want to organize.

Example for macOS:

```text
/Users/yourname/Desktop/MyMedia
```

Example for Windows:

```text
C:\Users\yourname\Desktop\MyMedia
```

You can also drag a folder into the Terminal window on macOS to insert its path.

### Step 5: Check the result

Once the script finishes, it will display the number of photos and videos moved, along with the locations of the destination folders.

Your selected root folder will now contain the organized `Photos` and `Videos` folders.

## 5. Safety and limitations

SortMyMedia does not delete media files intentionally. However, it moves them from their original locations, so review the destination folders after execution.

The script does not currently:
- Sort files by date, year, or month.
- Identify media based on actual file content rather than extensions.
- Detect duplicate content when files have different names.
- Organize audio files or documents.

These features can be added in future versions.
