from pickle import NONE


class Book:

    def __init__(self,title, author=NONE):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'{self.title} is written by {self.author}')

b = Book('hp','jk')
b.print_info()