"""
WebCrawler - Movie Rating Analyzer

This module processes movie data from text files and enriches it with IMDB ratings
using the IMDbPie API. It sorts movies by their IMDB ratings and outputs the
results to files.

Dependencies:
    - requests: For HTTP requests
    - beautifulsoup4: For web scraping (not actively used in current version)
    - imdbpie: For IMDB API interactions

Author: rasifmahmud
"""

import requests
import string
from bs4 import BeautifulSoup
from imdbpie import Imdb
from operator import itemgetter, attrgetter, methodcaller

# Initialize IMDB API client
imdb = Imdb()
imdb = Imdb(anonymize=True)  # Use proxy requests for privacy
imdb = Imdb(cache=True)      # Enable caching for better performance




def sort_upon_rating(movie_list):
    """
    Sort movies by their IMDB ratings in descending order.
    
    Args:
        movie_list (list): List of movie strings in format "name###year###rating###newline"
    
    Returns:
        list: Sorted list with highest rated movies first
    """
    temp_list = []
    # Parse movie data from strings
    for movie in movie_list:
        temp_list.append(movie.split("###"))

    # Sort by rating (index 2) in descending order
    sorted_list = sorted(temp_list, key=itemgetter(2))
    sorted_list.reverse()
    
    final_list = []
    temp_list = []
    
    # Reconstruct movie strings and separate movies with/without ratings
    for movie in sorted_list:
        if len(movie) >= 4:
            if movie[2] is not None:
                temp_list.append(movie[0] + "###" + movie[1] + "###" + movie[2] + movie[3])
            else:
                final_list.append(movie[0] + "###" + movie[1] + "###" + movie[2] + movie[3])

    return final_list + temp_list







def traverse():
    """
    Process the movie list file and enrich it with IMDB ratings.
    
    Reads from 'movie_list2.txt', extracts movie names and years,
    fetches IMDB ratings for each movie, and returns a sorted list.
    
    Returns:
        list: List of movies with ratings, sorted by rating in descending order
    """
    file = open('movie_list2.txt', 'r')
    movie_lines = file.readlines()
    file.close()
    
    final_list = []
    
    for line in movie_lines:
        # Skip empty lines
        if len(line) < 2:
            continue

        # Extract movie name and year from the line
        parts = line.split("###")
        name = parts[0][:len(parts[0])-1]  # Remove trailing character
        year = parts[1][:4]  # Extract first 4 characters as year
        
        # Fetch IMDB rating
        rating = get_movie_rating(name, year)
        print(f"Processing: {name} ({year}) - Rating: {rating}")
        
        # Add to final list with rating
        final_list.append(f"{name}####{year}####{str(rating)}####\n")

    # Sort movies by rating and return
    final_list = sort_upon_rating(final_list)
    return final_list


def get_movie_rating(name, year):
    """
    Fetch IMDB rating for a specific movie.
    
    Args:
        name (str): Movie title
        year (str): Release year
    
    Returns:
        str: IMDB rating as string, or '0' if movie not found
    """
    try:
        # Search for the movie on IMDB
        search_results = imdb.search_for_title(name)
        
        # Look for exact match by title and year
        for result in search_results:
            if result['title'] == name and result['year'] == year:
                movie_id = result['imdb_id']
                title = imdb.get_title_by_id(movie_id)
                return title.rating
    except Exception as e:
        print(f"Error fetching rating for {name} ({year}): {e}")
    
    # Return '0' if movie not found or error occurred
    return '0'


def write_all():
    """
    Main function that processes movies and writes results to file.
    
    Calls traverse() to get sorted movie list and writes it to 'final_movie_list'.
    """
    file = open('final_movie_list', 'w')
    file.writelines(traverse())
    file.close()
    print("Movie processing complete. Results saved to 'final_movie_list'")


if __name__ == "__main__":
    # Run the main processing function
    write_all()
    # Example usage for testing individual movie rating
    # print(get_movie_rating('A Better Life','2011'))