# Automatic File Sorter

A powerful Python script that automatically organizes files into folders based on their file types and extensions.

## Features

- **Smart Categorization**: Automatically sorts files into logical categories (Images, Documents, Videos, etc.)
- **Safe Operation**: Handles file conflicts by adding number suffixes
- **Dry Run Mode**: Preview changes before actually moving files
- **Recursive Sorting**: Option to sort files in subdirectories
- **Customizable**: Easy to modify file categories and rules
- **Statistics**: Shows detailed summary of operations
- **Cross-Platform**: Works on Windows, macOS, and Linux

## File Categories

The sorter organizes files into these categories:

- **Images**: jpg, png, gif, svg, webp, etc.
- **Documents**: pdf, doc, txt, rtf, etc.
- **Spreadsheets**: xlsx, csv, ods, etc.
- **Presentations**: ppt, pptx, key, etc.
- **Videos**: mp4, avi, mov, mkv, etc.
- **Audio**: mp3, wav, flac, aac, etc.
- **Archives**: zip, rar, 7z, tar, etc.
- **Code**: py, js, html, css, java, etc.
- **Executables**: exe, msi, deb, dmg, etc.
- **Fonts**: ttf, otf, woff, etc.

Files with unknown extensions are sorted into folders named after their extension.

## Usage

### Basic Usage

```bash
# Sort files in current directory
python file_sorter.py

# Preview what would be sorted (recommended first step)
python file_sorter.py --dry-run

# List all files and their detected categories
python file_sorter.py --list
```

### Advanced Usage

```bash
# Sort specific directory
python file_sorter.py --source ~/Downloads

# Sort to a different target directory
python file_sorter.py --source ~/Downloads --target ~/Organized

# Sort recursively through subdirectories
python file_sorter.py --recursive

# Combine options
python file_sorter.py --source ~/Downloads --target ~/Organized --dry-run
```

### Command Line Options

- `--source, -s`: Source directory to sort (default: current directory)
- `--target, -t`: Target directory for organized files (default: same as source)
- `--dry-run, -d`: Preview changes without moving files
- `--recursive, -r`: Sort files in subdirectories recursively
- `--list, -l`: List files and their detected categories

## Quick Start

1. **Create demo files for testing:**
   ```bash
   python demo_files.py
   ```

2. **Preview the sorting:**
   ```bash
   python file_sorter.py --dry-run
   ```

3. **List file categories:**
   ```bash
   python file_sorter.py --list
   ```

4. **Actually sort the files:**
   ```bash
   python file_sorter.py
   ```

## Safety Features

- **Conflict Resolution**: If a file with the same name exists, adds a number suffix
- **Skip System Files**: Automatically skips hidden files and system files
- **Error Handling**: Continues operation even if individual files fail to move
- **Dry Run**: Always test with `--dry-run` first
- **Statistics**: Shows exactly what was moved, skipped, or failed

## Customization

You can easily customize the file categories by editing the `file_categories` dictionary in the `FileSorter` class:

```python
self.file_categories = {
    'Images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'},
    'Documents': {'.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'},
    # Add your own categories here
    'MyCustomCategory': {'.custom', '.special'},
}
```

## Examples

### Organize Downloads Folder
```bash
python file_sorter.py --source ~/Downloads --dry-run
python file_sorter.py --source ~/Downloads
```

### Clean Up Desktop
```bash
python file_sorter.py --source ~/Desktop --target ~/Desktop/Organized
```

### Recursive Organization
```bash
python file_sorter.py --source ~/Documents --recursive --dry-run
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## License

This project is open source and available under the MIT License.