#!/usr/bin/env python3
"""
Demo File Creator (Safe Version)
Creates sample files for testing the file sorter with fallbacks for missing modules
"""

import os
import sys

# Safe pathlib alternative
try:
    from pathlib import Path
    HAS_PATHLIB = True
except ImportError:
    HAS_PATHLIB = False
    print("Warning: pathlib not available, using os.path fallback")

class SafePath:
    """Fallback Path class when pathlib is not available"""
    def __init__(self, path):
        self.path = str(path)
    
    def exists(self):
        return os.path.exists(self.path)
    
    def touch(self):
        """Create empty file"""
        try:
            with open(self.path, 'a'):
                pass
        except Exception as e:
            raise Exception(f"Could not create file {self.path}: {e}")

def create_demo_files():
    """Create sample files for testing the file sorter"""
    
    demo_files = [
        # Images
        'vacation_photo.jpg',
        'screenshot.png',
        'logo.svg',
        'profile_pic.gif',
        
        # Documents
        'report.pdf',
        'notes.txt',
        'presentation.docx',
        'manual.rtf',
        
        # Spreadsheets
        'budget.xlsx',
        'data.csv',
        'inventory.ods',
        
        # Videos
        'movie.mp4',
        'tutorial.avi',
        'clip.mov',
        
        # Audio
        'song.mp3',
        'podcast.wav',
        'sound_effect.flac',
        
        # Archives
        'backup.zip',
        'files.tar.gz',
        'package.rar',
        
        # Code
        'script.py',
        'webpage.html',
        'styles.css',
        'app.js',
        
        # Executables
        'installer.exe',
        'program.msi',
        
        # Fonts
        'custom_font.ttf',
        'web_font.woff',
        
        # Misc
        'readme.md',
        'config.json',
        'database.db',
        'unknown_file',  # File without extension
    ]
    
    print("Creating demo files for testing...")
    print("-" * 40)
    
    created_count = 0
    for filename in demo_files:
        if HAS_PATHLIB:
            file_path = Path(filename)
        else:
            file_path = SafePath(filename)
        
        # Don't overwrite existing files
        if file_path.exists():
            print(f"Skipped: {filename} (already exists)")
            continue
        
        try:
            # Create empty file
            file_path.touch()
            print(f"Created: {filename}")
            created_count += 1
        except Exception as e:
            print(f"Error creating {filename}: {e}")
    
    print(f"\nCreated {created_count} demo files!")
    print("\nNow you can test the file sorter with:")
    print("  python file_sorter_safe.py --dry-run    # Preview sorting")
    print("  python file_sorter_safe.py --list       # List file categories")
    print("  python file_sorter_safe.py              # Actually sort files")

if __name__ == "__main__":
    create_demo_files()