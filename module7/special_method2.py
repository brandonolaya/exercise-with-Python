#I have the next class and you print with function "len" the number the pages at the book

class Book():
    def __init__(self, title, author, amount_page):
        self.title = title
        self.author = author
        self.amount_page = amount_page

    def __len__(self):
        return self.amount_page

my_book = Book("la polla", "el pollitas", 523)
print(len(my_book))