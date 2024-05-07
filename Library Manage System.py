# I've got a good skeleton for this application.
# It still has some flaws, few function don't run as expected. 
# I have a meeting with Sarah on Thursday to look over it as I don't seem to be able to debug it myself.


from user import User
from book import Book
from author import Author


def main():

    thomas = User("Thomas Johnson", "NM987445")
    alchemist = Book("The Alchemist", "Paulo Coelho", "9781940313092", "novel", "1988")
    coelho = Author("Paulo Coelho", "Story of life")

    books = [alchemist]
    users = [thomas]
    authors = [coelho]
    current_user = None
    current_book = None
    print("Welcome to the Library Management System!")

    while True:
        print(books)
        action = input(
            """
    1. Book Ops
    2. User Ops
    3. Author Ops
    4. Quit
    > """
        )

        if action == "1":
            current_book = book_ops(books, current_user)
        elif action == "2":
            current_user = user_ops(users)
        elif action == "3":
            author = author_ops(authors)
        elif action == "4":
            break
        else:
            print("Invalid input.")


def borrow_book(self, book):
    if self.borrow_book == book:
        book.is_available = False
        print(f"{self.name} has borrowed {book.get_info()}")
    elif not book.is_available:
        print(f"{book.title} is not available.")
    else:
        self.borrow_book is not None
        print("You can not borrow more books.")


def return_book(self):
    if self.borrow_book is None:
        print(f"{self.name} does not have books to return.")
    else:
        self.borrow_book.is_available = True
        print(f"{self.name} returned {self.borrow_book.get_info()}.")
        self.borrow_book = None


def book_ops(books, current_user):

    while True:
        action = input(
            """
        1. Add Book
        2. Borrow 
        3. Return
        4. Search 
        5. Display all
        > """
        )

        if action == "1":
            new_book = add_book()
            books.append(new_book)
            return new_book
        elif action == "2":
            for idx, book in enumerate(books):
                if book.is_available:
                    print(f"{idx+1}.) {book.get_info()}")
            book = input("Book title: ")
            current_user.borrow_book(book)
            return None
        elif action == "3":
            if current_user.borrow_book:
                current_user.return_book()
                return None
            else:
                print("You do not have a book to return")
                return current_user
        elif action == "4":
            book = search_book(books)
            return book
        elif action == "5":
            return books
        else:
            print("Invalid input.")


def add_book():

    title = input("Title: ").title()
    author = input("Author: ").title()
    isbn = input("ISBN: #")
    genre = input("Genre: ")
    publication_date = input("Publication date: ")
    new_book = Book(title, author, isbn, genre, publication_date)
    print("Book added.")
    new_book.get_info()
    return new_book


def search_book(books):

    while True:
        title = input("Search Title: ").title()
        for book in books:
            if book.title == title:
                print("Book found!")
                book.get_info()
                return book
            else:
                print("No book found.")


def user_ops(users):

    while True:
        action = input(
            """
    1. Add new user
    2. View user details
    3. Display all
    > """
        )

        if action == "1":
            new_user = add_user()
            users.append(new_user)
            return new_user
        elif action == "2":
            user = search_user(users)
            return user
        elif action == "3":
            return users
        else:
            print("Invalid input.")


def add_user():
    name = input("Name: ").title()
    library_id = input("Library ID: ")
    new_user = User(name, library_id)
    print("User Added.")
    new_user.get_info()
    return new_user


def search_user(users):
    while True:
        name = input("Search Name: ").title()
        for user in users:
            if user.name == name:
                print("User found!")
                return user.get_info()


def author_ops(authors):

    while True:
        action = input(
            """
    1. Add new author
    2. View author
    3. Display all
    > """
        )

        if action == "1":
            new_author = add_author(authors)
            authors.append(new_author)
            return new_author
        elif action == "2":
            author = search_author(authors)
            return author
        elif action == "3":
            return authors
        else:
            print("Invalid input.")


def add_author(authors):
    author = input("Author's name: ").title()
    biography = input("Biography: ").title()
    new_author = Author(author, biography)
    print("Author added.")
    new_author.get_info()
    return new_author


def search_author(authors):
    while True:
        theauthor = input("Search Name: ").title()
        for author in authors:
            if author == theauthor:
                print("Author found!")
                return author.get_info()
            else:
                print("Author not found.")


main()
