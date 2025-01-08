# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {', '.join(book.title for book in self.borrowed_books)}"


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")

        book = self.find_book(book_title)
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found.")

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")

        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"Member '{member_name}' has exceeded the borrowing limit.")

        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"'{book_title}' has been borrowed by {member_name}.")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")

        book = self.find_book(book_title)
        if not book or book not in member.borrowed_books:
            raise ValueError(f"Book '{book_title}' is not borrowed by {member_name}.")

        book.is_borrowed = False
        member.borrowed_books.remove(book)
        print(f"'{book_title}' has been returned by {member_name}.")


# Testing the Library System
library = Library()

# Adding books
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

# Adding members
library.add_member("Alice")
library.add_member("Bob")

try:
    # Borrowing books
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "The Great Gatsby")
    
    # Attempt to borrow a fourth book
    library.borrow_book("Alice", "Nonexistent Book")  # Should raise BookNotFoundException

except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(e)

try:
    # Attempt to borrow a book already borrowed
    library.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException

except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(e)

# Returning books
library.return_book("Alice", "1984")

# Try borrowing again after returning
library.borrow_book("Bob", "1984")