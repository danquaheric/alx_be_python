class Book:
    """
    A simple Book class that demonstrates Python magic methods:
    __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a farewell message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        User-friendly string representation of the Book.
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the Book that can recreate the object.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"