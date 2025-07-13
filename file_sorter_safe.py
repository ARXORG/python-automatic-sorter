#!/usr/bin/env python3
"""
Automatic File Sorter (Safe Version)
Organizes files into folders based on their extensions with fallbacks for missing modules
"""

import os
import sys
from typing import Dict, List, Set
import argparse
from datetime import datetime

# Safe imports with fallbacks
try:
    from pathlib import Path
    HAS_PATHLIB = True
except ImportError:
    HAS_PATHLIB = False
    print("Warning: pathlib not available, using os.path fallback")

try:
    import shutil
    HAS_SHUTIL = True
except ImportError:
    HAS_SHUTIL = False
    print("Warning: shutil not available, using basic file operations")

class SafePath:
    """Fallback Path class when pathlib is not available"""
    def __init__(self, path):
        self.path = os.path.abspath(str(path))
        self.name = os.path.basename(self.path)
        self.suffix = os.path.splitext(self.path)[1]
        self.stem = os.path.splitext(self.name)[0]
        self.parent = SafePath(os.path.dirname(self.path))
    
    def __str__(self):
        return self.path
    
    def __truediv__(self, other):
        return SafePath(os.path.join(self.path, str(other)))
    
    def exists(self):
        return os.path.exists(self.path)
    
    def is_file(self):
        return os.path.isfile(self.path)
    
    def is_dir(self):
        return os.path.isdir(self.path)
    
    def iterdir(self):
        """List directory contents"""
        if not self.is_dir():
            return []
        try:
            return [SafePath(os.path.join(self.path, item)) 
                   for item in os.listdir(self.path)]
        except OSError:
            return []
    
    def mkdir(self, exist_ok=False):
        """Create directory"""
        try:
            os.makedirs(self.path, exist_ok=exist_ok)
        except OSError as e:
            if not (exist_ok and self.exists()):
                raise e
    
    def resolve(self):
        """Return absolute path"""
        return SafePath(os.path.abspath(self.path))
    
    def relative_to(self, other):
        """Return relative path"""
        return os.path.relpath(self.path, str(other))

def safe_move(source, destination):
    """Safe file move with fallbacks"""
    source_path = str(source)
    dest_path = str(destination)
    
    if HAS_SHUTIL:
        shutil.move(source_path, dest_path)
    else:
        # Fallback: copy then delete
        try:
            # Simple copy for small files
            with open(source_path, 'rb') as src:
                with open(dest_path, 'wb') as dst:
                    dst.write(src.read())
            os.remove(source_path)
        except Exception as e:
            raise Exception(f"Could not move file: {e}")

class FileSorter:
    """Main file sorting class with customizable rules and safety features"""
    
    def __init__(self, source_dir: str = ".", target_dir: str = None):
        if HAS_PATHLIB:
            self.source_dir = Path(source_dir).resolve()
            self.target_dir = Path(target_dir).resolve() if target_dir else self.source_dir
        else:
            self.source_dir = SafePath(source_dir).resolve()
            self.target_dir = SafePath(target_dir).resolve() if target_dir else self.source_dir
        
        # Predefined file type categories
        self.file_categories = {
            'Images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'},
            'Documents': {'.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'},
            'Spreadsheets': {'.xls', '.xlsx', '.csv', '.ods', '.numbers'},
            'Presentations': {'.ppt', '.pptx', '.odp', '.key'},
            'Videos': {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'},
            'Audio': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'},
            'Archives': {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'},
            'Code': {'.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'},
            'Executables': {'.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg', '.app'},
            'Fonts': {'.ttf', '.otf', '.woff', '.woff2', '.eot'}
        }
        
        # Files to skip (system files, hidden files, etc.)
        self.skip_files = {'.DS_Store', 'Thumbs.db', 'desktop.ini', '.gitignore', '.gitkeep'}
        self.skip_extensions = {'.tmp', '.temp', '.log'}
        
        # Statistics
        self.stats = {
            'moved': 0,
            'skipped': 0,
            'errors': 0,
            'categories_created': set()
        }
    
    def get_file_category(self, file_extension: str) -> str:
        """Determine the category for a file based on its extension"""
        file_extension = file_extension.lower()
        
        for category, extensions in self.file_categories.items():
            if file_extension in extensions:
                return category
        
        # If no category found, use the extension name (without dot)
        return file_extension[1:].upper() if file_extension else 'NO_EXTENSION'
    
    def should_skip_file(self, file_path) -> bool:
        """Check if a file should be skipped"""
        # Skip hidden files (starting with .)
        if file_path.name.startswith('.') and file_path.name not in self.skip_files:
            return True
        
        # Skip specific files
        if file_path.name in self.skip_files:
            return True
        
        # Skip specific extensions
        if file_path.suffix.lower() in self.skip_extensions:
            return True
        
        # Skip if it's the script itself
        if file_path.name in ['file_sorter.py', 'file_sorter_safe.py']:
            return True
        
        return False
    
    def create_category_folder(self, category: str):
        """Create a folder for the given category"""
        folder_path = self.target_dir / category
        folder_path.mkdir(exist_ok=True)
        self.stats['categories_created'].add(category)
        return folder_path
    
    def move_file_safely(self, source, destination) -> bool:
        """Move file with conflict resolution"""
        try:
            # If destination exists, add a number suffix
            if destination.exists():
                counter = 1
                stem = destination.stem
                suffix = destination.suffix
                parent = destination.parent
                
                while destination.exists():
                    new_name = f"{stem}_{counter}{suffix}"
                    destination = parent / new_name
                    counter += 1
            
            safe_move(source, destination)
            return True
            
        except Exception as e:
            print(f"Error moving {source.name}: {e}")
            self.stats['errors'] += 1
            return False
    
    def sort_files(self, dry_run: bool = False) -> None:
        """Main sorting function"""
        print(f"{'DRY RUN: ' if dry_run else ''}Sorting files in: {self.source_dir}")
        print(f"Target directory: {self.target_dir}")
        print("-" * 50)
        
        # Get all files in source directory (non-recursive by default)
        files_to_sort = [f for f in self.source_dir.iterdir() 
                        if f.is_file() and not self.should_skip_file(f)]
        
        if not files_to_sort:
            print("No files to sort!")
            return
        
        print(f"Found {len(files_to_sort)} files to sort")
        print()
        
        for file_path in files_to_sort:
            category = self.get_file_category(file_path.suffix)
            
            if dry_run:
                print(f"Would move: {file_path.name} → {category}/")
                continue
            
            # Create category folder
            category_folder = self.create_category_folder(category)
            destination = category_folder / file_path.name
            
            # Move the file
            if self.move_file_safely(file_path, destination):
                print(f"Moved: {file_path.name} → {category}/")
                self.stats['moved'] += 1
            else:
                self.stats['skipped'] += 1
        
        if not dry_run:
            self.print_summary()
    
    def print_summary(self) -> None:
        """Print sorting statistics"""
        print("\n" + "=" * 50)
        print("SORTING COMPLETE!")
        print("=" * 50)
        print(f"Files moved: {self.stats['moved']}")
        print(f"Files skipped: {self.stats['skipped']}")
        print(f"Errors: {self.stats['errors']}")
        print(f"Categories created: {len(self.stats['categories_created'])}")
        
        if self.stats['categories_created']:
            print(f"Categories: {', '.join(sorted(self.stats['categories_created']))}")
        
        print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def list_file_types(self) -> None:
        """List all files and their detected categories"""
        print(f"File analysis for: {self.source_dir}")
        print("-" * 50)
        
        files = [f for f in self.source_dir.iterdir() 
                if f.is_file() and not self.should_skip_file(f)]
        
        if not files:
            print("No files found!")
            return
        
        # Group files by category
        categories = {}
        for file_path in files:
            category = self.get_file_category(file_path.suffix)
            if category not in categories:
                categories[category] = []
            categories[category].append(file_path.name)
        
        # Print grouped results
        for category in sorted(categories.keys()):
            print(f"\n{category}:")
            for filename in sorted(categories[category]):
                print(f"  • {filename}")
        
        print(f"\nTotal files: {len(files)}")
        print(f"Categories: {len(categories)}")


def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(
        description="Automatic File Sorter - Organize files by type (Safe Version)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python file_sorter_safe.py                    # Sort current directory
  python file_sorter_safe.py --dry-run          # Preview what would be sorted
  python file_sorter_safe.py --list             # List file types
  python file_sorter_safe.py --source ~/Downloads --target ~/Organized
        """
    )
    
    parser.add_argument('--source', '-s', 
                       default='.',
                       help='Source directory to sort (default: current directory)')
    
    parser.add_argument('--target', '-t',
                       help='Target directory for sorted files (default: same as source)')
    
    parser.add_argument('--dry-run', '-d',
                       action='store_true',
                       help='Preview changes without moving files')
    
    parser.add_argument('--list', '-l',
                       action='store_true',
                       help='List files and their detected categories')
    
    args = parser.parse_args()
    
    # Create file sorter instance
    sorter = FileSorter(args.source, args.target)
    
    try:
        if args.list:
            sorter.list_file_types()
        else:
            sorter.sort_files(args.dry_run)
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    print("File Sorter (Safe Version)")
    print("Using fallbacks for missing Python modules")
    print()
    main()