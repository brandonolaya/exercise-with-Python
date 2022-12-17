
class Book():
    def __init__(self, title, author, amount_page):
        self.title = title
        self.author = author
        self.amount_page = amount_page

        
    def __del__(self):
        print("Libro eliminado")