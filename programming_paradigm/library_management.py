from book import Book

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        """Adds a new book to the library."""
        book = Book(title, author)
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it's available in the library."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f'You have checked out "{book.title}".'
                else:
                    return f'"{book.title}" is currently checked out.'
        return f'Book titled "{title}" is not found in the library.'

    def return_book(self, title):
        """Returns a book by title if it was checked out."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f'You have returned "{book.title}".'
                else:
                    return f'"{book.title}" was not checked out.'
        return f'Book titled "{title}" is not found in the library.'

    def list_available_books(self):
        """Lists all books currently available in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            return '\n'.join([str(book) for book in available_books])
        return "No books are currently available."

