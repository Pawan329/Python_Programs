class Library:

    available_books = ["machine learning", "sql", "python", "docker"]

    def borrowBook(self):
        book_name = input("[Borrow] Please enter book name: ")
        
        if book_name not in self.available_books:
            print("**Please enter a valid book name** \n Press 'q' to quit")
            if book_name == "q": 
                return None
            else:
                Library.borrowBook(self)

        else:
            self.available_books.remove(book_name)
        

    def returnBook(self):
        pass

    def donateBook(self):
        pass


action = Library()

action.borrowBook()
print("Available books: ",action.available_books)