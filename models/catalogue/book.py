class Book:
    def __init__(book_id, self, isbn, author, title, publisher, publication_date, num_pages):
        self.id = book_id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.num_pages = num_pages
        
    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author