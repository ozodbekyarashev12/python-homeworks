# Custom Exception for Book Not Found
class BookNotFoundException(Exception):
    def __init__(self, message="Book not found in the library"):
        self.message = message
        super().__init__(self.message)

# Custom Exception for Book Already Borrowed
class BookAlreadyBorrowedException(Exception):
    def __init__(self, message="The book has already been borrowed"):
        self.message = message
        super().__init__(self.message)

# Custom Exception for Member Borrow Limit Exceeded
class MemberLimitExceededException(Exception):
    def __init__(self, message="Member cannot borrow more than 3 books"):
        self.message = message
        super().__init__(self.message)

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException()
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise ValueError(f"{book.title} is not borrowed by {self.name}")

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, title):
        # Find the book by title
        book = next((b for b in self.books if b.title == title), None)
        if not book:
            raise BookNotFoundException(f"Book '{title}' not found in the library.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{title}' is already borrowed.")
        member.borrow_book(book)

    def return_book(self, member, title):
        # Find the book by title
        book = next((b for b in self.books if b.title == title), None)
        if not book:
            raise BookNotFoundException(f"Book '{title}' not found in the library.")
        member.return_book(book)

# Test the Library Management System
if __name__ == "__main__":
    # Create books
    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")
    book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    # Create a library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Create a member
    member = Member("John Doe")
    library.add_member(member)

    try:
        # Borrow books
        library.borrow_book(member, "The Catcher in the Rye")
        print(f"{member.name} borrowed 'The Catcher in the Rye'.")

        library.borrow_book(member, "1984")
        print(f"{member.name} borrowed '1984'.")

        library.borrow_book(member, "To Kill a Mockingbird")
        print(f"{member.name} borrowed 'To Kill a Mockingbird'.")

        # This should raise an exception because the member can borrow only 3 books
        library.borrow_book(member, "The Great Gatsby")
    except MemberLimitExceededException as e:
        print(f"Error: {e}")

    try:
        # Try borrowing a book that is already borrowed
        library.borrow_book(member, "The Catcher in the Rye")
    except BookAlreadyBorrowedException as e:
        print(f"Error: {e}")

    try:
        # Try borrowing a book that does not exist
        library.borrow_book(member, "Moby Dick")
    except BookNotFoundException as e:
        print(f"Error: {e}")

    # Return books
    library.return_book(member, "1984")
    print(f"{member.name} returned '1984'.")

    try:
        # Try returning a book that was not borrowed
        library.return_book(member, "The Great Gatsby")
    except ValueError as e:
        print(f"Error: {e}")
