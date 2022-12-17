#I have the next class and I want that when I call it and print the title and the author

class Book():
    def __init__(self, title, author, amount_page):
        self.title = title
        self.author = author
        self.amount_page = amount_page
        
    def __str__(self):
        return f'"{self.title}", de {self.author}'

my_book = Book("la polla", "el pollitas", 523)
print(my_book)