from abc import ABC, abstractmethod

class BookSearch(ABC):    
    @abstractmethod
    def search_by_title(self, title):
        pass
        
    @abstractmethod
    def search_by_author(self, author):
        pass
        
    @abstractmethod
    def search_by_genre(self, genre):
        pass
        
    @abstractmethod
    def search_by_isbn(self, isbn):
        pass