class BookShelf:
    def __init__(self, *books):
        self.books= books

    def __str__(self):
        return f"BookSheft with {len(self.books)} books."
    
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Book {self.name}"
    

book = Book("Harry Potter")
book2 = Book("Python 101")
sheft = BookShelf(book, book2)

print(sheft)