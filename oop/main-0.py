from library_system import Book, EBook, PrintBook, Library

def main():
    # Creating a Library instance
    my_Library = Library()
    
    # Creating instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
   
    # Adding books to the library
    my_Library.add_book(classic_book)
    my_Library.add_book(digital_novel)
    my_Library.add_book(paper_novel)
    
    # List all books in the library
    my_Library.list_books()
    
if __name__ == "__main__":
    main()