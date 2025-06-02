# Library Book Management System

books = {
    "1984": {"author": "Orwell", "available": True},
    "Dracula": {"author": "Stoker", "available": True},
    "Frankenstein": {"author": "Shelley", "available": False}
}

borrowed_books = []

def view_books():
    print("\n📚 All Books in the Library:")
    for title, info in books.items():
        status = "Available " if info["available"] else "Borrowed "
        print(f'"{title}" by {info["author"]} - {status}')
    print()

def borrow_book():
    book_title = input("Enter the book title to borrow: ").strip().lower()
    for title in books:
        if title.lower() == book_title:
            if books[title]["available"]:
                books[title]["available"] = False
                borrowed_books.append(title)
                print(f'You have borrowed "{title}"\n')
                return
            else:
                print(f'Sorry, "{title}" is already borrowed.\n')
                return
    print("Book not found in the library.\n")

def return_book():
    book_title = input("Enter the book title to return: ").strip().lower()
    for title in books:
        if title.lower() == book_title:
            if not books[title]["available"]:
                books[title]["available"] = True
                borrowed_books.remove(title)
                print(f'You have returned "{title}".\n')
                return
            else:
                print(f'"{title}" was not borrowed.\n')
                return
    print("Book not found in the library.\n")

def add_book():
    title = input("Enter the new book title: ").strip()
    author = input("Enter the author name: ").strip()
    if title in books:
        print("Book already exists in the library.\n")
    else:
        books[title] = {"author": author, "available": True}
        print(f'Book "{title}" by {author} added to the library.\n')

def view_borrowed_books():
    if not borrowed_books:
        print("No books are currently borrowed.\n")
        return
    print("\nBorrowed Books:")
    for title in borrowed_books:
        print(f'"{title}" by {books[title]["author"]}')
    print()

def main():
    print("Welcome to the Library System")
    while True:
        print("\n1. View Books\n2. Borrow Book\n3. Return Book\n4. Add New Book\n5. View Borrowed Books\n6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            view_borrowed_books()
        elif choice == '6':
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
