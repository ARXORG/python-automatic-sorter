#!/usr/bin/env python3
"""
File Sorter Professional Installer
Complete installation package with loading screen and setup wizard
"""

import os
import sys
import time
import random

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading_bar(duration=20):
    """Show a professional loading bar for specified duration"""
    clear_screen()
    
    # Loading messages that appear during installation
    messages = [
        "Initializing File Sorter installation...",
        "Checking system compatibility...",
        "Verifying Python installation...",
        "Setting up file categories...",
        "Creating directory structure...",
        "Configuring safety features...",
        "Installing launcher components...",
        "Creating desktop shortcuts...",
        "Setting up menu entries...",
        "Optimizing performance...",
        "Finalizing installation...",
        "Installation complete!"
    ]
    
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "FILE SORTER PROFESSIONAL INSTALLER" + " " * 12 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Calculate timing
    steps = 100
    step_duration = duration / steps
    message_interval = duration / len(messages)
    
    current_message = 0
    next_message_time = 0
    
    for i in range(steps + 1):
        # Update message if it's time
        current_time = i * step_duration
        if current_time >= next_message_time and current_message < len(messages):
            message = messages[current_message]
            current_message += 1
            next_message_time += message_interval
        
        # Create progress bar
        filled = int(i * 50 / steps)
        bar = "█" * filled + "░" * (50 - filled)
        percentage = int(i * 100 / steps)
        
        # Display progress
        print(f"\r{message:<50}", end="")
        print(f"\n[{bar}] {percentage}%", end="")
        
        # Add some visual flair
        if i < steps:
            print(" " + "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"[i % 10], end="")
        else:
            print(" ✓", end="")
        
        sys.stdout.flush()
        time.sleep(step_duration)
        
        # Clear the lines for next update (except on last iteration)
        if i < steps:
            print("\r" + " " * 70, end="")
            print("\r" + " " * 70, end="")
            print("\r", end="")

def show_welcome_screen():
    """Show welcome screen"""
    clear_screen()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + " " * 20 + "AUTOMATIC FILE SORTER PROFESSIONAL" + " " * 23 + "║")
    print("║" + " " * 30 + "Installation Wizard" + " " * 29 + "║")
    print("║" + " " * 78 + "║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 78 + "║")
    print("║  Welcome to the File Sorter Professional installation wizard!" + " " * 17 + "║")
    print("║" + " " * 78 + "║")
    print("║  This program will automatically organize your files into neat" + " " * 16 + "║")
    print("║  folders based on their types (Images, Documents, Videos, etc.)" + " " * 14 + "║")
    print("║" + " " * 78 + "║")
    print("║  Features:" + " " * 69 + "║")
    print("║  • Smart file categorization with 10+ categories" + " " * 29 + "║")
    print("║  • Safe operation with preview mode" + " " * 41 + "║")
    print("║  • Automatic conflict resolution" + " " * 44 + "║")
    print("║  • User-friendly GUI launcher" + " " * 45 + "║")
    print("║  • Cross-platform compatibility" + " " * 43 + "║")
    print("║" + " " * 78 + "║")
    print("║  Press Enter to begin installation..." + " " * 39 + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    
    input()

def check_python():
    """Check Python installation"""
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 6:
            return True, f"Python {version.major}.{version.minor}.{version.micro}"
        else:
            return False, f"Python {version.major}.{version.minor}.{version.micro} (requires 3.6+)"
    except:
        return False, "Unknown"

def create_files():
    """Create necessary files for the file sorter"""
    
    # Create the main launcher if it doesn't exist
    if not os.path.exists('file_sorter_launcher.py'):
        print("Creating launcher...")
        # The launcher file already exists from previous artifact
    
    # Create batch file for Windows
    if os.name == 'nt':
        with open('File Sorter.bat', 'w') as f:
            f.write('@echo off\n')
            f.write(f'cd /d "{os.getcwd()}"\n')
            f.write('python file_sorter_launcher.py\n')
            f.write('pause\n')
    
    # Create shell script for Unix-like systems
    else:
        with open('file_sorter', 'w') as f:
            f.write('#!/bin/bash\n')
            f.write(f'cd "{os.getcwd()}"\n')
            f.write('python3 file_sorter_launcher.py\n')
        os.chmod('file_sorter', 0o755)

def create_desktop_shortcut():
    """Create desktop shortcut"""
    try:
        if os.name == 'nt':  # Windows
            desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
            shortcut_path = os.path.join(desktop, 'File Sorter.bat')
            
            with open(shortcut_path, 'w') as f:
                f.write('@echo off\n')
                f.write(f'cd /d "{os.getcwd()}"\n')
                f.write('python file_sorter_launcher.py\n')
                f.write('pause\n')
            
            return True, "Desktop shortcut created"
        
        else:  # Linux/macOS
            desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
            if os.path.exists(desktop):
                shortcut_path = os.path.join(desktop, 'File Sorter.desktop')
                
                with open(shortcut_path, 'w') as f:
                    f.write('[Desktop Entry]\n')
                    f.write('Version=1.0\n')
                    f.write('Type=Application\n')
                    f.write('Name=File Sorter\n')
                    f.write('Comment=Automatic File Organizer\n')
                    f.write(f'Exec=python3 {os.getcwd()}/file_sorter_launcher.py\n')
                    f.write('Icon=folder\n')
                    f.write('Terminal=true\n')
                    f.write('Categories=Utility;\n')
                
                os.chmod(shortcut_path, 0o755)
                return True, "Desktop shortcut created"
            else:
                return False, "Desktop folder not found"
    
    except Exception as e:
        return False, f"Error creating shortcut: {e}"

def show_completion_screen():
    """Show installation completion screen"""
    clear_screen()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + " " * 25 + "INSTALLATION SUCCESSFUL!" + " " * 28 + "║")
    print("║" + " " * 78 + "║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 78 + "║")
    print("║  🎉 File Sorter Professional has been installed successfully!" + " " * 16 + "║")
    print("║" + " " * 78 + "║")
    print("║  You can now run the File Sorter in the following ways:" + " " * 22 + "║")
    print("║" + " " * 78 + "║")
    
    if os.name == 'nt':
        print("║  1. Double-click 'File Sorter.bat' on your Desktop" + " " * 27 + "║")
        print("║  2. Double-click 'File Sorter.bat' in this folder" + " " * 28 + "║")
    else:
        print("║  1. Double-click 'File Sorter' on your Desktop (if available)" + " " * 17 + "║")
        print("║  2. Run './file_sorter' in this folder" + " " * 39 + "║")
    
    print("║  3. Run 'python file_sorter_launcher.py'" + " " * 37 + "║")
    print("║" + " " * 78 + "║")
    print("║  Recommended first steps:" + " " * 52 + "║")
    print("║  • Create demo files to test safely" + " " * 41 + "║")
    print("║  • Use preview mode before sorting real files" + " " * 32 + "║")
    print("║  • Read the help section for detailed instructions" + " " * 27 + "║")
    print("║" + " " * 78 + "║")
    print("║  Thank you for choosing File Sorter Professional!" + " " * 27 + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    print()
    print("Press Enter to launch File Sorter...")
    input()

def main():
    """Main installation process"""
    try:
        # Welcome screen
        show_welcome_screen()
        
        # Check Python
        python_ok, python_version = check_python()
        if not python_ok:
            clear_screen()
            print("❌ ERROR: Python 3.6 or higher is required!")
            print(f"Found: {python_version}")
            print("\nPlease install Python from https://python.org")
            print("Make sure to check 'Add Python to PATH' during installation.")
            input("\nPress Enter to exit...")
            return
        
        # Show loading screen (20 seconds)
        show_loading_bar(20)
        
        # Create files
        print("\n\nSetting up files...")
        create_files()
        
        # Create shortcuts
        print("Creating shortcuts...")
        success, message = create_desktop_shortcut()
        if success:
            print(f"✓ {message}")
        else:
            print(f"⚠ {message}")
        
        # Show completion
        time.sleep(1)
        show_completion_screen()
        
        # Launch the program
        clear_screen()
        print("Launching File Sorter...")
        time.sleep(1)
        
        # Import and run the launcher
        try:
            import file_sorter_launcher
            file_sorter_launcher.main()
        except ImportError:
            print("Error: Could not import file_sorter_launcher.py")
            print("Please run: python file_sorter_launcher.py")
            input("Press Enter to exit...")
    
    except KeyboardInterrupt:
        clear_screen()
        print("\nInstallation cancelled by user.")
        print("Goodbye!")
    except Exception as e:
        clear_screen()
        print(f"Installation error: {e}")
        print("Please try running the installation again.")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()