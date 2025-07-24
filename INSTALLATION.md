# Installation Guide

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/rasifmahmud/WebCrawler.git
   cd WebCrawler
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your movie data in `movie_list2.txt`:
   ```
   The Shawshank Redemption###1994
   The Godfather###1972
   Pulp Fiction###1994
   ```

4. Run the crawler:
   ```bash
   python main.py
   ```

## Virtual Environment (Recommended)

For better dependency management, use a virtual environment:

```bash
# Create virtual environment
python -m venv webcrawler_env

# Activate virtual environment
# On Windows:
webcrawler_env\Scripts\activate
# On macOS/Linux:
source webcrawler_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Troubleshooting Installation

### Python Version Issues
Ensure you're using Python 3.6 or higher:
```bash
python --version
```

### Dependency Conflicts
If you encounter dependency conflicts:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### API Access Issues
The IMDbPie library requires internet access. Ensure your network allows HTTPS connections to IMDB.