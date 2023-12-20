class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    # Phương thức lớp là một phương thức được gắn liền với lớp chứ không phải với một đối tượng cụ thể của lớp. Nó có thể được gọi trực tiếp từ tên lớp mà không cần tạo đối tượng.
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)
    
    @classmethod
    def create_book(cls, name: str, book_type: str, weight: int) -> "Book":
        if book_type.lower() not in cls.TYPES:
            raise ValueError(f"Invalid book type. Must be one of {cls.TYPES}")
        
        return cls(name, book_type.lower(), weight)

# Sử dụng phương thức tạo sách thông qua trọng lượng
book_by_weight = Book.create_book("Python Handbook", "paperback", 300)
print(book_by_weight)