class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def drop_book(self, title):
        self.books = [b for b in self.books if b.title != title]

    def display_books(self):
        for b in self.books:
            print(f"{b.title} by {b.author}")

# Example
lib = Library()
lib.add_book("Henry", "DAN JONES")
lib.add_book("The Eagle and the Hart", "Helen_caster")
lib.add_book("we the people", "jill lepore")
lib.display_books()
lib.drop_book("Henry")
print("After drop:")
lib.display_books()
