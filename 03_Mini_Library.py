class Library:
    available_books = ["ml", "python", "DSA", "sql"]
    def borrowBook(self):
        book_name = input("[Borrow] Please enter book name: ")

        if book_name not in self.available_books:
            print("**Please enter a valid book name** \n Press 'q' to quit")
            if book_name == "q": 
                return None
            else:
                print("Available books are: ",self.available_books)
                Library.borrowBook(self)

        else:
            self.available_books.remove(book_name)
            print("Available books are: ",self.available_books)
        

    def returnBook(self):
        book_name = input("Enter book name: ")
        self.available_books.append(book_name)
        print("Available books are: ",self.available_books)
        

    def donateBook(self):
        book_name = input("Please enter the book name: ")
        self.available_books.append(book_name)
        print("Available books are: ",self.available_books)
        


action = Library()

user_input = int(input("Select: \n1. To Borrow book \n2. To return book \n3. To Donate book \n4. To see list of available books\n"))
if user_input == 1:
    action.borrowBook()

elif user_input == 2:
    action.returnBook()

elif user_input == 3:
    action.donateBook()

elif user_input == 4:
    print(action.available_books)