class User():
    
    def __init__(self, name, library_id, borrow_book=None):
        self.name = name
        self.library_id = library_id
        self.borrow_book = borrow_book
        
    def get_info(self):
        print(f'User name: {self.name}, library_id: {self.library_id}, {self.borrow_book}')
        
    def borrow_book(self, book):
        if self.borrow_book == book:
            book.is_available = False
            print(f'{self.name} has borrowed {book.get_info()}')
        else:
            self.borrow_book != None
            print('You can not borrow more books.')
            
    def return_book(self):
        self.borrow_book.is_available = True
        print(f'{self.name} returned {self.borrow_book.get_info()}')
        self.borrow_book = None
            
        