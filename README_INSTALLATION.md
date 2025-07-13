# File Sorter Installation Guide

This guide will help you set up and use the Automatic File Sorter on your computer.

## Quick Start

### Windows Users
1. **Download all files** to a folder on your computer
2. **Double-click `install.bat`** to install
3. **Use the desktop shortcut** or run `python file_sorter_launcher.py`

### Linux/macOS Users
1. **Download all files** to a folder on your computer
2. **Open terminal** in the folder
3. **Run:** `chmod +x install.sh && ./install.sh`
4. **Use:** `./file_sorter` or `python3 file_sorter_launcher.py`

## What Gets Installed

The installation creates:
- **Desktop shortcut** (Windows/Linux)
- **Start menu entry** (Windows)
- **Applications menu entry** (Linux)
- **Launcher scripts** for easy access

## How to Use

### Option 1: Easy GUI Launcher
Run `python file_sorter_launcher.py` for a user-friendly menu with options:
1. Create demo files for testing
2. Preview file sorting (safe mode)
3. List files by category
4. Sort files in current directory
5. Sort files from custom directory
6. Help & instructions

### Option 2: Command Line
```bash
# Create test files
python run_demo.py

# Preview what would be sorted (recommended first step)
python file_sorter_safe.py --dry-run

# List files by category
python file_sorter_safe.py --list

# Actually sort files
python file_sorter_safe.py

# Sort specific directory
python file_sorter_safe.py --source /path/to/messy/folder
```

## File Categories

The sorter organizes files into these folders:
- **Images**: jpg, png, gif, svg, webp, etc.
- **Documents**: pdf, doc, txt, rtf, etc.
- **Videos**: mp4, avi, mov, mkv, etc.
- **Audio**: mp3, wav, flac, aac, etc.
- **Archives**: zip, rar, 7z, tar, etc.
- **Code**: py, js, html, css, etc.
- **Spreadsheets**: xlsx, csv, ods, etc.
- **Presentations**: ppt, pptx, key, etc.
- **Executables**: exe, msi, deb, dmg, etc.
- **Fonts**: ttf, otf, woff, etc.

## Safety Features

- **Dry Run Mode**: Preview changes before moving files
- **Conflict Resolution**: Adds numbers to duplicate filenames
- **Skip System Files**: Ignores hidden and system files
- **Error Handling**: Continues even if some files fail
- **Detailed Statistics**: Shows what was moved, skipped, or failed

## Recommended Workflow

1. **Test First**: Create demo files and test the sorter
2. **Preview**: Always use dry-run mode first
3. **Backup**: Make a backup of important files
4. **Sort**: Run the actual sorting operation

## Troubleshooting

### Python Not Found
- **Windows**: Install Python from python.org, check "Add to PATH"
- **Linux**: `sudo apt install python3` (Ubuntu/Debian)
- **macOS**: Install from python.org or use Homebrew

### Permission Errors
- **Windows**: Run as Administrator
- **Linux/macOS**: Use `sudo` if needed, or change file permissions

### Files Not Moving
- Check if files are in use by other programs
- Ensure you have write permissions to the target directory
- Use dry-run mode to see what would happen

## Uninstallation

To remove the File Sorter:
1. Delete the folder containing all the files
2. Delete desktop shortcuts (if created)
3. Remove start menu entries (Windows) or application entries (Linux)

## Support

If you encounter issues:
1. Try the safe version: `file_sorter_safe.py`
2. Use dry-run mode to test: `--dry-run`
3. Check file permissions and Python installation
4. Make sure Python 3.6+ is installed

## Advanced Usage

### Custom Categories
Edit `file_sorter_safe.py` and modify the `file_categories` dictionary to add your own file types.

### Recursive Sorting
Use the command line version with `--recursive` to sort subdirectories.

### Different Target Directory
Specify a different output directory with `--target /path/to/organized/folder`.