from user import User
from book import Book
from author import Author

thomas = User('Thomas Johnson', 'NM987445')
alchemist = Book('The Alchemist', 'Paulo Coelho', '9781940313092', 'novel', '1988')


def main():
    books = [alchemist]
    users = [thomas]
    authors = []
    current_user = None
    current_book = None
    print ('Welcome to the Library Management System!')
    
    while True:
        print(books)
        action = input('''
    1. Book Ops
    2. User Ops
    3. Author Ops
    4. Quit
    > ''')
        
        
        if action == '1':
            book = book_ops(books, current_user)
        elif action == '2':
            current_user = user_ops(users)
        elif action == '3':
            author = author_ops(authors)
        elif action == '4':
            break
        else:
            print('Invalid input.')

    
    def book_ops(books, current_user):
        
        while True:
            action = input('''
        1. Add Book
        2. Borrow 
        3. Return
        4. Search 
        5. Display all
        > ''')
            
            if action == '1':
                new_book = add_book()
                books.append(new_book)
                return new_book
            elif action == '2':
                for idx, book in enumerate(books):
                    if book.is_available:
                        print(f'{idx+1}.) {book.get_info()}') 
                book = input('Book title: ')
                current_user.borrow(book)
                return None
            elif action == '3':
                if current_user.borrow_book:
                    current_user.return_book()
                    return None
                else:
                    print('You do not have a book to return')
                    return current_user
            elif action == '4':
                book = search_book(books)
                return book
            elif action == '5':
                return books
            else:
                print('Invalid input.')
                  
            
    def add_book():
        title = input('Title: ').title()
        author = input('Author: ').title()
        new_book = book(title, author)
        print('Book added.')
        new_book.get_info()
        return new_book
    
    def search_book(books):

        while True:
            title = input('Search Title: ').title()
            for book in books:
                if book.title == title:
                    print('Book found!')
                    book.get_info()
                    return book
                elif book.title != title:
                    print('No book found.')
                    continue
   
                
    def user_ops(users):
        
        while True:
            action = input('''
        1. Add new user
        2. View user details
        3. Display all
        > ''')
            
            if action == '1':
                new_user = add_user()
                users.append(new_user)
                return new_user
            elif action == '2':
                user = search_user(users)
                return user
            elif action == '3':
                return users
            else:
                print('Invalid input.')
                
                
    def add_user():
        name = input('Name: ').title()
        address = input('Address: ').title()
        phone = input('Phone: ')
        new_user = User(name, address, phone)
        print('User Added.')
        new_user.get_info()
        return new_user
    
    
    def search_user(users):
        while True:
            name = input('Search Name: ').title()
            for user in users:
             if user.name == name:
                print('User found!')
                user.get_info()
                return user
    
    def author_ops():
        
        while True:
            action = input('''
        1. Add new author
        2. View author
        3. Display all
        > ''')
            
            if action == '1':
                new_author = add_author()
                users.append(new_author)
                return new_author
            elif action == '2':
                user = search_author(author)
                return author
            elif action == '3':
                return author
            else:
                print('Invalid input.')
                
                
    def add_author():
        name = input('Name: ').title()
        new_author = Author(name)
        print('Author added.')
        new_author.get_info()
        return new_author
    
    
    def search_author(authors):
        while True:
            name = input('Search Name: ').title()
            for author in authors:
             if author.name == name:
                print('Author found!')
                author.get_info()
                return author
        

main()