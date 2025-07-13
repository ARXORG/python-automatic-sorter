#!/usr/bin/env python3
"""
Simple Demo Runner
Runs the file sorter demo without problematic imports
"""

import os

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
        # Don't overwrite existing files
        if os.path.exists(filename):
            print(f"Skipped: {filename} (already exists)")
            continue
        
        try:
            # Create empty file
            with open(filename, 'w') as f:
                f.write('')
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