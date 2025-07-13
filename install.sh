#!/bin/bash
# File Sorter Installation Script for Linux/macOS
# This script sets up the file sorter and creates shortcuts

echo "========================================"
echo "   File Sorter Installation Script"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed"
        echo "Please install Python 3.6 or higher"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "Python found!"
$PYTHON_CMD --version

echo
echo "Setting up File Sorter..."

# Make scripts executable
chmod +x file_sorter_launcher.py
chmod +x file_sorter_safe.py
chmod +x run_demo.py

# Create launcher script
cat > file_sorter << 'EOF'
#!/bin/bash
# File Sorter Launcher
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
python3 file_sorter_launcher.py
EOF

chmod +x file_sorter

# Try to create desktop shortcut (Linux with desktop environment)
if [ -d "$HOME/Desktop" ]; then
    cat > "$HOME/Desktop/File Sorter.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=File Sorter
Comment=Automatic File Organizer
Exec=$(pwd)/file_sorter
Icon=folder
Terminal=true
Categories=Utility;
EOF
    chmod +x "$HOME/Desktop/File Sorter.desktop"
    echo "Desktop shortcut created"
fi

# Try to create applications menu entry (Linux)
if [ -d "$HOME/.local/share/applications" ]; then
    cat > "$HOME/.local/share/applications/file-sorter.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=File Sorter
Comment=Automatic File Organizer
Exec=$(pwd)/file_sorter
Icon=folder
Terminal=true
Categories=Utility;
EOF
    echo "Applications menu entry created"
fi

echo
echo "========================================"
echo "        Installation Complete!"
echo "========================================"
echo
echo "The File Sorter has been installed successfully!"
echo
echo "You can now run it by:"
echo "1. Double-clicking 'File Sorter' on your Desktop (if available)"
echo "2. Running: ./file_sorter"
echo "3. Running: $PYTHON_CMD file_sorter_launcher.py"
echo
echo "To uninstall, simply delete this folder and any shortcuts."
echo