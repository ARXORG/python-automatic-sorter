#!/usr/bin/env python3
"""
File Sorter Launcher
Easy-to-use GUI launcher for the file sorter
"""

import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Display the main menu"""
    clear_screen()
    print("=" * 60)
    print("           AUTOMATIC FILE SORTER LAUNCHER")
    print("=" * 60)
    print()
    print("Choose an option:")
    print()
    print("1. Create demo files for testing")
    print("2. Preview file sorting (dry run)")
    print("3. List files by category")
    print("4. Sort files in current directory")
    print("5. Sort files from custom directory")
    print("6. Help & Instructions")
    print("7. Exit")
    print()
    print("-" * 60)

def get_user_choice():
    """Get user menu choice"""
    while True:
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return int(choice)
            else:
                print("Invalid choice. Please enter a number between 1-7.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
        except Exception:
            print("Invalid input. Please enter a number between 1-7.")

def run_command(command):
    """Run a system command and wait for user input"""
    print(f"\nRunning: {command}")
    print("-" * 40)
    os.system(command)
    print("-" * 40)
    input("\nPress Enter to continue...")

def create_demo_files():
    """Create demo files"""
    print("Creating demo files...")
    run_command("python run_demo.py")

def preview_sorting():
    """Preview file sorting"""
    print("Previewing file sorting (no files will be moved)...")
    run_command("python file_sorter_safe.py --dry-run")

def list_files():
    """List files by category"""
    print("Analyzing files by category...")
    run_command("python file_sorter_safe.py --list")

def sort_current_directory():
    """Sort files in current directory"""
    print("Sorting files in current directory...")
    print("WARNING: This will actually move files!")
    confirm = input("Are you sure? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        run_command("python file_sorter_safe.py")
    else:
        print("Operation cancelled.")
        input("Press Enter to continue...")

def sort_custom_directory():
    """Sort files from custom directory"""
    print("Sort files from custom directory")
    print("-" * 30)
    source = input("Enter source directory path: ").strip()
    if not source:
        print("No directory specified.")
        input("Press Enter to continue...")
        return
    
    target = input("Enter target directory (optional, press Enter for same as source): ").strip()
    
    command = f"python file_sorter_safe.py --source \"{source}\""
    if target:
        command += f" --target \"{target}\""
    
    print(f"\nWARNING: This will move files from {source}")
    confirm = input("Are you sure? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        run_command(command)
    else:
        print("Operation cancelled.")
        input("Press Enter to continue...")

def show_help():
    """Show help and instructions"""
    clear_screen()
    print("=" * 60)
    print("                    HELP & INSTRUCTIONS")
    print("=" * 60)
    print()
    print("WHAT THIS PROGRAM DOES:")
    print("• Automatically sorts files into folders by type")
    print("• Creates folders like 'Images', 'Documents', 'Videos', etc.")
    print("• Handles file conflicts by adding numbers to filenames")
    print("• Safe operation with preview mode")
    print()
    print("FILE CATEGORIES:")
    print("• Images: jpg, png, gif, svg, etc.")
    print("• Documents: pdf, doc, txt, rtf, etc.")
    print("• Videos: mp4, avi, mov, mkv, etc.")
    print("• Audio: mp3, wav, flac, aac, etc.")
    print("• Archives: zip, rar, 7z, tar, etc.")
    print("• Code: py, js, html, css, etc.")
    print("• And many more...")
    print()
    print("RECOMMENDED WORKFLOW:")
    print("1. Create demo files (option 1) to test safely")
    print("2. Preview sorting (option 2) to see what would happen")
    print("3. List files (option 3) to see categories")
    print("4. Actually sort files (option 4 or 5)")
    print()
    print("SAFETY FEATURES:")
    print("• Dry run mode shows changes without moving files")
    print("• Skips system files and hidden files")
    print("• Handles duplicate names automatically")
    print("• Shows detailed statistics after sorting")
    print()
    input("Press Enter to return to main menu...")

def main():
    """Main program loop"""
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 1:
            create_demo_files()
        elif choice == 2:
            preview_sorting()
        elif choice == 3:
            list_files()
        elif choice == 4:
            sort_current_directory()
        elif choice == 5:
            sort_custom_directory()
        elif choice == 6:
            show_help()
        elif choice == 7:
            clear_screen()
            print("Thank you for using the File Sorter!")
            print("Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nProgram interrupted by user.")
        print("Goodbye!")
        sys.exit(0)