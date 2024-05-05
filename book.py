class Book():
    
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.is_available = True
        
    def get_info(self):
        return f'{self.title}, {self.author}, {self.isbn}, {self.genre}, {self.publication_date}.'