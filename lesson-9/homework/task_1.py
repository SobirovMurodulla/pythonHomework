class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book titled '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise ValueError(f"Member named '{name}' not found in the library.")

if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "Nonexistent Book")  # Should raise BookNotFoundException
    except Exception as e:
        print(e)

    try:
        library.return_book("Alice", "1984")
        library.borrow_book("Bob", "1984")
        library.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException
    except Exception as e:
        print(e)

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "Another Book")  # Should raise MemberLimitExceededException
    except Exception as e:
        print(e)