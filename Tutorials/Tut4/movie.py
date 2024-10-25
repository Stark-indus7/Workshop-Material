import os

# File where the movie data will be stored
MOVIE_DB_FILE = "movies.txt"


def load_movies():
    """Loads movie data from the file into a list of dictionaries."""
    movies = []
    if os.path.exists(MOVIE_DB_FILE):
        with open(MOVIE_DB_FILE, "r") as file:
            for line in file:
                title, director, year = line.strip().split(",")
                movies.append({"title": title, "director": director, "year": year})
    return movies


def save_movies(movies):
    """Saves the movie data from the list into the file."""
    with open(MOVIE_DB_FILE, "w") as file:
        for movie in movies:
            file.write(f"{movie['title']},{movie['director']},{movie['year']}\n")


def add_movie(movies):
    """Adds a new movie to the database."""
    title = input("Enter movie title: ").strip()
    director = input("Enter movie director: ").strip()
    year = input("Enter release year: ").strip()

    if not title or not director or not year.isdigit():
        print("Invalid input. Please enter valid data for title, director, and year.")
        return

    movies.append({"title": title, "director": director, "year": year})
    save_movies(movies)
    print(f"Movie '{title}' added successfully!")


def display_movies(movies):
    """Displays all movies in the database."""
    if not movies:
        print("No movies found in the database.")
        return

    print("\nMovie Database:")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie['title']} (Director: {movie['director']}, Year: {movie['year']})")


def search_movie(movies):
    """Searches for a movie by title."""
    search_title = input("Enter movie title to search: ").strip().lower()

    found_movies = [movie for movie in movies if search_title in movie['title'].lower()]

    if found_movies:
        print("\nSearch Results:")
        for movie in found_movies:
            print(f"{movie['title']} (Director: {movie['director']}, Year: {movie['year']})")
    else:
        print(f"No movie found with title '{search_title}'.")


def main():
    """Main function to run the movie database system."""
    movies = load_movies()

    while True:
        print("\nMovie Database Management System")
        print("1. Add Movie")
        print("2. Display Movies")
        print("3. Search Movie")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            display_movies(movies)
        elif choice == '3':
            search_movie(movies)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()






# import os

# os.mkdir("D:\\Workshop\\Workshop-Material\\Projects")
# os.mkdir("D:\\Workshop\\Workshop-Material\\Projects_For_Workshop")
# os.removedirs("D:\\Workshop\\Workshop-Material\\Projects_For_Workshop")
# os.remove("D:\\Workshop\\Workshop-Material\\Tutorials\\create.py")


