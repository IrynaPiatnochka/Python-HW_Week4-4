class User():
    
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrow_book = None
        
    def get_info(self):
        return f'User name: {self.name}, Library_id: {self.library_id}, {self.borrow_book}'
    
    
        
    
        