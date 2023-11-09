from models.catalogue.book import Book

class BookItem(Book):
    def __init__(self, book_id, ISBN, author, title, publisher, publication_date, num_pages, book_item_id, is_borrowed=False, due_date=None):
        super().__init__(book_id, ISBN, author, title, publisher, publication_date, num_pages)
        self.book_item_id = book_item_id
        self.is_borrowed = is_borrowed
        self.due_date = due_date
        
    def get_due_date(self):
        return self.due_date
    
    def set_due_date(self, due_date):
        self.due_date = due_date
        
    def get_borrowed_status(self):
        return self.is_borrowed
    
    def set_borrowed_status(self, is_borrowed):
        self.is_borrowed = is_borrowed