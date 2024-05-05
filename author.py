class Author():
    
    def __init__(self, author, biograpy):
        self.author = author
        self.biography = biograpy
        self.is_available = True
        
    def get_info(self):
        return f'{self.author}, {self.biography}'