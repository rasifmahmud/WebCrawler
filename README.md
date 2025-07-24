# WebCrawler

A Python-based web crawler and movie rating analyzer that processes movie data from text files and enriches it with IMDB ratings to create sorted movie lists.

## Features

- Reads movie data from text files
- Fetches movie ratings from IMDB using the IMDbPie API
- Sorts movies by their IMDB ratings in descending order
- Handles movie name and year matching
- Outputs processed data to files for further use

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install requests beautifulsoup4 imdbpie
```

## Project Structure

```
WebCrawler/
├── README.md              # This documentation file
├── requirements.txt       # Python dependencies
├── main.py               # Main crawler script
├── demo.py               # Movie sorting utility
├── movie_list2.txt       # Input movie data (name###year format)
├── final_movie_list      # Output sorted movie list
├── temp_movie_list       # Temporary processing file
└── rating                # Rating data file
```

## Usage

### Basic Usage

1. **Prepare your movie data**: Ensure your movie list is in the correct format in `movie_list2.txt`:
   ```
   Movie Name###Year
   The Shawshank Redemption###1994
   The Godfather###1972
   ```

2. **Run the main crawler**:
   ```bash
   python main.py
   ```

3. **Check results**: The sorted movie list will be saved to `final_movie_list` with ratings:
   ```
   The Shawshank Redemption###1994###9.3
   The Godfather###1972###9.2
   ```

### Advanced Usage

**Sort existing movie data** (if you already have ratings):
```bash
python demo.py
```

## File Formats

### Input Format (`movie_list2.txt`)
Each line should contain:
```
MovieName###Year
```

### Output Format (`final_movie_list`)
Each line contains:
```
MovieName###Year###Rating
```

## API Reference

### Main Functions

#### `get_movie_rating(name, year)`
Fetches the IMDB rating for a specific movie.

**Parameters:**
- `name` (str): Movie title
- `year` (str): Release year

**Returns:**
- `str`: IMDB rating or '0' if not found

#### `sort_upon_rating(list)`
Sorts a list of movies by their IMDB ratings.

**Parameters:**
- `list` (list): List of movie strings in format "name###year###rating"

**Returns:**
- `list`: Sorted list with highest rated movies first

#### `traverse()`
Processes the movie list file and enriches it with IMDB ratings.

**Returns:**
- `list`: List of movies with ratings

## Configuration

The crawler uses IMDbPie with the following settings:
- Anonymous requests (to protect privacy)
- Caching enabled (for better performance)

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **API rate limiting**: The IMDB API may rate limit requests. The script includes caching to minimize API calls.

3. **Movie not found**: If a movie isn't found on IMDB, it will receive a rating of '0'

4. **File permissions**: Ensure the script has read/write permissions for the data files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source. Please check the repository for license information.

## Notes

- The crawler is designed to work with movie data files in a specific format
- IMDB data is fetched using the IMDbPie library
- Results are cached to improve performance on subsequent runs
