"""
Movie Data Sorting Utility

This module provides utilities for sorting movie data that already includes ratings.
It's designed to work with movie data in the format "Name Year Rating".

Author: rasifmahmud
"""

from operator import itemgetter, attrgetter, methodcaller


def to_str(word_list):
    """
    Convert a list of words to a single space-separated string.
    
    Args:
        word_list (list): List of strings to join
    
    Returns:
        str: Space-separated string of all words
    """
    result = ''
    for word in word_list:
        result += word + ' '

    return result[:len(result)-1]  # Remove trailing space




def sort_upon_rating():
    """
    Sort movies by their ratings and write results to file.
    
    Reads movie data from 'temp_movie_list', sorts by rating in descending order,
    and writes the sorted results to 'bal' file.
    """
    temp_list = return_data_list()

    # Sort by rating (index 2) in descending order
    sorted_list = sorted(temp_list, key=itemgetter(2))
    sorted_list.reverse()
    
    final_list = []
    temp_list = []
    
    # Reconstruct movie strings with proper spacing
    for movie in sorted_list:
        if len(movie) >= 4:
            if movie[2] is not None:
                temp_list.append(movie[0] + "   " + movie[1] + "   " + movie[2] + movie[3])
            else:
                final_list.append(movie[0] + "   " + movie[1] + "   " + movie[2] + movie[3])

    # Write sorted results to file
    result = final_list + temp_list
    file = open('bal', 'w')
    file.writelines(result)
    file.close()
    print("Sorting complete. Results saved to 'bal'")





def return_data_list():
    """
    Parse movie data from temp_movie_list file.
    
    Reads movie data in format "Movie Name Year Rating" from 'temp_movie_list'
    and converts it to a structured list format.
    
    Returns:
        list: List of movie data where each item is [name, year, rating, newline]
    """
    file = open('temp_movie_list', 'r')
    lines = file.readlines()
    file.close()
    
    final_list = []
    
    for line in lines:
        words = line.split(' ')
        
        # Process lines with at least 3 parts (name, year, rating)
        if len(words) > 2:
            # Reconstruct movie name (all words except last 2)
            name = to_str(words[:len(words) - 2])
            year = words[len(words) - 2]
            rating = words[len(words) - 1]
            
            # Create structured movie data
            movie_data = [name, year, rating, "\n"]
            final_list.append(movie_data)
        else:
            print(f"Skipping malformed line: {line.strip()}")

    return final_list


if __name__ == "__main__":
    # Run the sorting function
    sort_upon_rating()