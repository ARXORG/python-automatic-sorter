@echo off
REM File Sorter Installation Script for Windows
REM This script sets up the file sorter and creates shortcuts

echo ========================================
echo    File Sorter Installation Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found!
python --version

echo.
echo Setting up File Sorter...

REM Create desktop shortcut
echo Creating desktop shortcut...
echo @echo off > "%USERPROFILE%\Desktop\File Sorter.bat"
echo cd /d "%~dp0" >> "%USERPROFILE%\Desktop\File Sorter.bat"
echo python file_sorter_launcher.py >> "%USERPROFILE%\Desktop\File Sorter.bat"
echo pause >> "%USERPROFILE%\Desktop\File Sorter.bat"

REM Create start menu shortcut
if not exist "%APPDATA%\Microsoft\Windows\Start Menu\Programs\File Sorter" (
    mkdir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\File Sorter"
)
echo @echo off > "%APPDATA%\Microsoft\Windows\Start Menu\Programs\File Sorter\File Sorter.bat"
echo cd /d "%~dp0" >> "%APPDATA%\Microsoft\Windows\Start Menu\Programs\File Sorter\File Sorter.bat"
echo python file_sorter_launcher.py >> "%APPDATA%\Microsoft\Windows\Start Menu\Programs\File Sorter\File Sorter.bat"

echo.
echo ========================================
echo         Installation Complete!
echo ========================================
echo.
echo The File Sorter has been installed successfully!
echo.
echo You can now run it by:
echo 1. Double-clicking "File Sorter" on your Desktop
echo 2. Finding "File Sorter" in your Start Menu
echo 3. Running: python file_sorter_launcher.py
echo.
echo To uninstall, simply delete the folder and shortcuts.
echo.
pause