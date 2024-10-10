class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,file_size):
        self.file_size = file_size 

class PrintBook(Book): 
    def __init__(self,page_count):
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)