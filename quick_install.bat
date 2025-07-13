@echo off
REM Quick File Sorter Installer for Windows
REM Double-click this file to install File Sorter Professional

title File Sorter Professional Installer

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ========================================
    echo    PYTHON NOT FOUND
    echo ========================================
    echo.
    echo Python is required to run File Sorter.
    echo.
    echo Please install Python from:
    echo https://python.org
    echo.
    echo Make sure to check "Add Python to PATH"
    echo during installation.
    echo.
    pause
    exit /b 1
)

REM Run the installer
python installer.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Installation encountered an error.
    pause
)