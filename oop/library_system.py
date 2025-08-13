class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} [Ebook, File Size: {self.file_size}MB]"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [PrintBook, Page Count: {self.page_count}]"
    
class Library:
    def __init__(self):
        self.books = []  #To list stored books

    def add_book(self, book):
        if isinstance(book, Book): #Only accept objects in the class Book
            self.books.append(book)
        else:
            print("Only Book objects can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)

        