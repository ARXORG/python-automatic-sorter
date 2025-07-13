#!/bin/bash
# Quick File Sorter Installer for Linux/macOS
# Run this script to install File Sorter Professional

echo "========================================"
echo "  File Sorter Professional Installer"
echo "========================================"

# Check if Python is installed
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo
    echo "ERROR: Python is not installed"
    echo
    echo "Please install Python 3.6 or higher:"
    echo "• Ubuntu/Debian: sudo apt install python3"
    echo "• macOS: Install from python.org or use Homebrew"
    echo "• Other: Check your package manager"
    echo
    exit 1
fi

# Make installer executable
chmod +x installer.py

# Run the installer
$PYTHON_CMD installer.py

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo
    echo "Installation encountered an error."
    echo "Press Enter to exit..."
    read
fi