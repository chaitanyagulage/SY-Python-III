class Book:
    """Represents a single book in the library."""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # A new book is available by default

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Patron:
    """Represents a library user."""
    
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []  # List to track books currently borrowed by the patron

    def __str__(self):
        return f"Patron: {self.name} (ID: {self.patron_id})"


class Library:
    """Manages the overall operations of books and patrons."""
    
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        """Adds a new book to the library collection."""
        self.books.append(book)
        print(f"Added to library: {book.title}")

    def register_patron(self, patron):
        """Registers a new patron with the library."""
        self.patrons.append(patron)
        print(f"Registered patron: {patron.name}")

    def find_book(self, isbn):
        """Helper method to find a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_patron(self, patron_id):
        """Helper method to find a patron by ID."""
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    def borrow_book(self, patron_id, isbn):
        """Handles the process of a patron borrowing a book."""
        patron = self.find_patron(patron_id)
        book = self.find_book(isbn)

        if not patron:
            print("Error: Patron not found.")
            return
        if not book:
            print("Error: Book not found in the library.")
            return

        if book.is_available:
            book.is_available = False
            patron.borrowed_books.append(book)
            print(f"Success: {patron.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently borrowed by someone else.")

    def return_book(self, patron_id, isbn):
        """Handles the process of a patron returning a book."""
        patron = self.find_patron(patron_id)
        book = self.find_book(isbn)

        if not patron or not book:
            print("Error: Invalid Patron ID or Book ISBN.")
            return

        if book in patron.borrowed_books:
            book.is_available = True
            patron.borrowed_books.remove(book)
            print(f"Success: {patron.name} returned '{book.title}'.")
        else:
            print(f"Error: {patron.name} does not have '{book.title}' borrowed.")

    def display_available_books(self):
        """Prints all currently available books."""
        print("\n--- Available Books ---")
        available_books = [book for book in self.books if book.is_available]
        
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
        print("-----------------------\n")


# ==========================================
# Example Usage (Driver Code)
# ==========================================
if __name__ == "__main__":
    # 1. Initialize the Library
    my_library = Library()

    # 2. Create and add books
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0345339683")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467")
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # 3. Register patrons
    patron1 = Patron("Alice Smith", "P01")
    patron2 = Patron("Bob Jones", "P02")
    
    my_library.register_patron(patron1)
    my_library.register_patron(patron2)

    # 4. Display initially available books
    my_library.display_available_books()

    # 5. Borrow books
    my_library.borrow_book("P01", "978-0345339683") # Alice borrows The Hobbit
    my_library.borrow_book("P02", "978-0345339683") # Bob tries to borrow The Hobbit (fails)
    my_library.borrow_book("P02", "978-0451524935") # Bob borrows 1984

    # 6. Display available books after borrowing
    my_library.display_available_books()

    # 7. Return books
    my_library.return_book("P01", "978-0345339683") # Alice returns The Hobbit
    
    # 8. Display final available books
    my_library.display_available_books()