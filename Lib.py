class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies  # Number of available copies
    
    def __repr__(self):
        return f"{self.book_id}: {self.title} by {self.author} (Copies: {self.copies})"


class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books using book_id as key
        self.users = {}  # Dictionary to store users (optional for enhancement)
    
    def add_book(self, book_id, title, author, copies):
        if book_id not in self.books:
            new_book = Book(book_id, title, author, copies)
            self.books[book_id] = new_book
            print(f"Book '{title}' added successfully!")
        else:
            print("Book already exists!")
    
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book ID {book_id} removed from library!")
        else:
            print("Book not found!")
    
    def borrow_book(self, book_id):
        if book_id in self.books and self.books[book_id].copies > 0:
            self.books[book_id].copies -= 1
            print(f"Book ID {book_id} borrowed!")
        else:
            print("Book not available!")

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id].copies += 1
            print(f"Book ID {book_id} returned!")
        else:
            print("Book not found!")
    
    def view_books(self):
        for book_id, book in self.books.items():
            print(book)

# Sample test
lib = Library()
lib.add_book(1, "Python Programming", "John Doe", 5)
lib.add_book(2, "Data Science", "Jane Smith", 3)

lib.view_books()

lib.borrow_book(1)
lib.return_book(1)
lib.view_books()

lib.remove_book(2)
