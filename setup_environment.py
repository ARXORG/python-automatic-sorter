#!/usr/bin/env python3
"""
Environment Setup Script
Creates a virtual environment and provides fallbacks for missing functionality
"""

import sys
import subprocess
import os

def setup_virtual_environment():
    """Create and activate a virtual environment"""
    print("Setting up Python virtual environment...")
    
    try:
        # Create virtual environment
        subprocess.run([sys.executable, '-m', 'venv', '.venv'], check=True)
        print("✓ Virtual environment created successfully")
        
        # Provide activation instructions
        if os.name == 'nt':  # Windows
            activate_cmd = '.venv\\Scripts\\activate'
        else:  # Unix-like systems
            activate_cmd = 'source .venv/bin/activate'
        
        print(f"\nTo activate the virtual environment, run:")
        print(f"  {activate_cmd}")
        print("\nThen run the scripts again:")
        print("  python demo_files.py")
        print("  python file_sorter.py --help")
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        print("Trying alternative approach...")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    
    return True

def check_python_installation():
    """Check if Python installation is working properly"""
    print("Checking Python installation...")
    
    # Test basic imports
    try:
        import pathlib
        print("✓ pathlib module available")
    except ImportError:
        print("✗ pathlib module missing")
        return False
    
    try:
        import os
        if hasattr(os, 'chmod'):
            print("✓ os.chmod available")
        else:
            print("✗ os.chmod missing")
            return False
    except ImportError:
        print("✗ os module missing")
        return False
    
    print(f"Python version: {sys.version}")
    return True

if __name__ == "__main__":
    print("Python Environment Diagnostic Tool")
    print("=" * 40)
    
    if check_python_installation():
        print("\n✓ Python installation appears to be working correctly")
        print("You can run the file sorter scripts directly.")
    else:
        print("\n✗ Python installation has issues")
        print("Attempting to create virtual environment...")
        
        if setup_virtual_environment():
            print("\n✓ Virtual environment setup complete")
        else:
            print("\n✗ Could not resolve Python environment issues")
            print("Please reinstall Python or contact system administrator")