import json

# File to store library data
FILE_NAME = "library.txt"

def load_library():
    """Load the library from a file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save the library to a file."""
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {"Title": title, "Author": author, "Year": year, "Genre": genre, "Read": read_status}
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book(library):
    """Search for books by title or author."""
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    query = input("Enter the search term: ").strip().lower()
    results = [book for book in library if query in book["Title"].lower() or query in book["Author"].lower()]
    
    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["Read"] else "Unread"
            print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["Read"] else "Unread"
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")

def display_statistics(library):
    """Display statistics about the library."""
    total_books = len(library)
    read_books = sum(book["Read"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def main():
    """Main function to run the menu system."""
    library = load_library()
    
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
