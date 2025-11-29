# library_management.py

class Book:
    """Represents a book with title, author, and checkout status."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out. Return True if succeeded, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned (available). Return True if succeeded, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is not currently checked out (i.e. available)."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book instances."""
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book: Book):
        """Add a Book instance to the library's collection."""
        # Optional: avoid duplicates by title + author; here we just append
        self._books.append(book)

    def check_out_book(self, title: str):
        """
        Attempt to check out a book with matching title.
        If found and available, mark it checked out and return True.
        If not found or already checked out, return False.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title: str):
        """
        Attempt to return a book with matching title.
        If found and currently checked out, mark it available and return True.
        Otherwise return False.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # book not found

    def list_available_books(self):
        """Print all books that are currently available (not checked out)."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
        else:
            for book in available:
                print(book)
