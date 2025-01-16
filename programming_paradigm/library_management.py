class Book:
    # A class representing a book in the library
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self):
        # Mark the book as checked out
        if not self._is_checked_out:
            return True
        return False
    
    def return_book(self):
        # Mark the book as returned
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        # Check if the book is available
        return not self._is_checked_out
    
class Library:
    # A class representing a library.
    
    def __init__(self):
        self.__books = []
        
    def add_book(self, book):
        # Add a book to the Library.
        if isinstance(book, Book):
            self.__books.append(book)
        
    def check_out_book(self, title):
        # Check out a book by its title.
        for book in self.__books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out '{title}' successfully.")
                return
        print(f"'{title}' is not available or does not exist.")
        
    def return_book(self, title):
        # Return a book by its title.
        for book in self.__books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                return
        print(f"'{title}' is not currently checked out or does not exist.")
        
    def list_available_books(self):
        # List all available books in the library.
        available_books = [book for book in self.__books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
        
        