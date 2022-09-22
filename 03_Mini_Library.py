


class Library:

    # library_file_read = open("Library.txt", "r")
    # library_file_write = open("Library.txt", "w")
    

    def borrowBook(self):
        book_name = input("[Borrow] Please enter book name: ")

        if book_name not in self.available_books:
            print("**Please enter a valid book name** \n Press 'q' to quit")
            if book_name == "q": 
                self.library_file.close()
                return None
            else:
                print("Available books are: ",self.available_books)
                Library.borrowBook(self)

        else:
            self.available_books.remove(book_name)
            print("Available books are: ",self.available_books)
            self.library_file.close()
        

    def returnBook(self):
        library_file_read = open("Library.txt","r")
        library = library_file_read.readlines()

        return_book = input("Enter book name: ")
        return_book = return_book + "\n"

        if return_book not in library:
            
            return_book_to_library = open("Library.txt","a+")
            return_book_to_library.writelines([return_book])
            library_file_read.close()
            return_book_to_library.close()

            Library.availableBooks(self)
            
        else:
            print("***Already returned***")

    def donateBook(self):
        book_name = input("Please enter the book name: ")
        library_file_append = open("Library.txt","a+")
        library_file_append.writelines([book_name, "\n"])
        library_file_append.close()

        Library.availableBooks(self)

    def availableBooks(self):
        all_books = open("Library.txt","r")
        books = all_books.readlines()
        print("Available Books: ",books)
        


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