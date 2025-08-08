#Manage books in a library using classes and OOP concepts.

class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute (starts as available)
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # It wasn't checked out

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """Represents the entire library collection."""

    def __init__(self):
        # Private list to store Book objects
        self._books = []

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f" '{title}' has been checked out.")
                return
        print(f" '{title}' is not available right now.")

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f" '{title}' has been returned.")
                return
        print(f" '{title}' was not checked out.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available at the moment.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
