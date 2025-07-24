# Usage Examples

## Basic Examples

### Example 1: Process a Simple Movie List

Create a file `movie_list2.txt` with the following content:
```
The Matrix###1999
Inception###2010
Interstellar###2014
```

Run the crawler:
```bash
python main.py
```

Expected output in `final_movie_list`:
```
Interstellar###2014###8.6
Inception###2010###8.8
The Matrix###1999###8.7
```

### Example 2: Using the Demo Script

If you have movie data with ratings already in `temp_movie_list`:
```
The Shawshank Redemption 1994 9.3
The Godfather 1972 9.2
The Dark Knight 2008 9.0
```

Run the demo script:
```bash
python demo.py
```

This will sort the movies and save them to the `bal` file.

## Advanced Usage

### Custom Input Processing

You can modify the input format by editing the parsing logic in `main.py`:

```python
# Current format: MovieName###Year
# To support different separators, modify the split operation:
parts = line.split("|||")  # Use ||| instead of ###
```

### Batch Processing Multiple Files

To process multiple movie lists:

```python
import main

# Save original function
original_traverse = main.traverse

def process_multiple_files(file_list):
    """Process multiple movie list files."""
    all_movies = []
    for filename in file_list:
        # Temporarily modify the input file
        main.traverse = lambda: process_file(filename)
        movies = main.traverse()
        all_movies.extend(movies)
    
    # Sort all movies together
    return main.sort_upon_rating(all_movies)

def process_file(filename):
    """Process a single file."""
    # Your processing logic here
    pass
```

### Error Handling

The crawler includes basic error handling, but you can enhance it:

```python
def safe_get_rating(name, year):
    """Get movie rating with retry logic."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return main.get_movie_rating(name, year)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                return '0'
```

## Output Formats

### Customizing Output Format

You can modify the output format in the `traverse()` function:

```python
# Current: name###year###rating###
# Custom format:
final_list.append(f"{name} ({year}) - Rating: {rating}\n")
```

### Converting to Different Formats

#### JSON Output
```python
import json

def export_to_json(movie_list, filename):
    """Export movie list to JSON format."""
    movies = []
    for movie_line in movie_list:
        parts = movie_line.strip().split("###")
        if len(parts) >= 3:
            movies.append({
                "title": parts[0],
                "year": int(parts[1]),
                "rating": float(parts[2]) if parts[2] != '0' else None
            })
    
    with open(filename, 'w') as f:
        json.dump(movies, f, indent=2)
```

#### CSV Output
```python
import csv

def export_to_csv(movie_list, filename):
    """Export movie list to CSV format."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Year', 'Rating'])
        
        for movie_line in movie_list:
            parts = movie_line.strip().split("###")
            if len(parts) >= 3:
                writer.writerow([parts[0], parts[1], parts[2]])
```