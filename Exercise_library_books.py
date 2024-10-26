class library:

    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books

    def get_books(self):
        print(self.books)

    def get_no_of_books(self):
        print(f"The library has {len(self.books)} books.")

    def add_book(self,new_book):
        self.no_of_books+=1
        self.books.append(new_book)


books_1= ["Bangla", "English", "Math"]
chawkbazar_library = library(3, books_1)

chawkbazar_library.add_book("Science")

chawkbazar_library.get_books()

chawkbazar_library.get_no_of_books()

       