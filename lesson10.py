# Solving the tasks with Python code using English variables and descriptions.

# Task 1: Create a dictionary where keys are music genres and values are lists with the names of the songs for each genre.
music_genres = {
    "Rock": ["Song1", "Song2"],
    "Pop": ["Song3", "Song4"],
    "Jazz": ["Song5", "Song6"]
}

def add_song_to_genre(genre, song):
    if genre in music_genres:
        music_genres[genre].append(song)
    else:
        music_genres[genre] = [song]

# Task 2: Create a dictionary to store students with a list of their grades. Write a function to calculate the average grade for each student.
students_grades = {
    "Alice": [80, 85, 88],
    "Bob": [78, 82, 79],
    "Charlie": [92, 90, 93]
}

def calculate_average_grade(student):
    grades = students_grades.get(student)
    if grades:
        return sum(grades) / len(grades)
    else:
        return "Student not found"

# Task 3: Create a list of lists representing a matrix. Implement any mathematical function.
def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Task 4: Create a dictionary where keys are book titles and values are dictionaries with information about each book. Implement a search by author.
books_info = {
    "Book1": {"author": "Author1", "year": 2000},
    "Book2": {"author": "Author2", "year": 2005},
    "Book3": {"author": "Author1", "year": 2010}
}

def find_books_by_author(author):
    return [title for title, info in books_info.items() if info["author"] == author]

# Task 5: Create a tuple with coordinates in three-dimensional space and write a function that accepts this tuple and returns the sum of all its coordinates.
def sum_of_coordinates(coordinates):
    return sum(coordinates)

# Demonstrate the usage of these functions and display the results.

# Add a new song to a genre
add_song_to_genre("Rock", "Song7")

# Calculate the average grade for a student
average_grade_alice = calculate_average_grade("Alice")

# Create a matrix and transpose it
sample_matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = matrix_transpose(sample_matrix)

# Find books by a specific author
books_by_author1 = find_books_by_author("Author1")

# Sum of coordinates
coordinates_tuple = (1, 2, 3)
coordinates_sum = sum_of_coordinates(coordinates_tuple)

print(music_genres, average_grade_alice, transposed_matrix, books_by_author1, coordinates_sum)
