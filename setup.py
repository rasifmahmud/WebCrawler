#!/usr/bin/env python3
"""
Setup script for WebCrawler

This script helps set up the WebCrawler environment and verify dependencies.
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is 3.6 or higher."""
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✓ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required dependencies."""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def verify_dependencies():
    """Verify that all dependencies are properly installed."""
    dependencies = [
        ('requests', 'requests'),
        ('beautifulsoup4', 'bs4'),
        ('imdbpie', 'imdbpie')
    ]
    
    all_installed = True
    for package_name, import_name in dependencies:
        try:
            if import_name == 'imdbpie':
                # Special check for imdbpie due to potential compatibility issues
                from imdbpie import Imdb
                print(f"✓ {package_name} is installed")
            else:
                __import__(import_name)
                print(f"✓ {package_name} is installed")
        except ImportError as e:
            print(f"✗ {package_name} is not installed or has compatibility issues")
            if import_name == 'imdbpie':
                print("  Note: imdbpie may have compatibility issues with newer Python versions")
                print("  Consider using 'cinemagoer' as an alternative")
            all_installed = False
    
    return all_installed

def check_input_file():
    """Check if the input file exists and has the correct format."""
    if not os.path.exists('movie_list2.txt'):
        print("⚠ Input file 'movie_list2.txt' not found")
        print("Creating a sample file...")
        create_sample_input()
    else:
        print("✓ Input file 'movie_list2.txt' found")

def create_sample_input():
    """Create a sample input file."""
    sample_content = """The Shawshank Redemption###1994
The Godfather###1972
The Dark Knight###2008
Pulp Fiction###1994
The Lord of the Rings: The Return of the King###2003
"""
    
    with open('movie_list2.txt', 'w') as f:
        f.write(sample_content)
    
    print("✓ Sample input file created")

def main():
    """Main setup function."""
    print("WebCrawler Setup")
    print("================")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Verify dependencies
    if not verify_dependencies():
        print("Some dependencies are missing. Please run 'pip install -r requirements.txt'")
        sys.exit(1)
    
    # Check input file
    check_input_file()
    
    print("\n✓ Setup complete!")
    print("\nYou can now run the WebCrawler:")
    print("  python main.py")

if __name__ == "__main__":
    main()