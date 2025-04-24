# Project: Simple Library System
# Student Name: Arav Neroth
# Date Completed: 4/24/2025

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def list_books(self):
        for book in self.books:
            print(book)
        print("\n")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                print(f"You have borrowed '{book.title}' \n")
                return
            
        print("Book is not available")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                print(f"You have returned '{book.title}' \n")
                return
            
        print("Book is not available")

library = Library("Downtown Library")

book1 = Book("Mistborn", "Brandon Sanderson", "83473847")
book2 = Book("The Well Of Ascension", "Brandon Sanderson", "83473467")
book3 = Book("The Hero Of Ages", "Brandon Sanderson", "83183847")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()
library.borrow_book("83183847")
library.list_books()
library.borrow_book("83473847")
library.return_book("83183847")
library.list_books()
