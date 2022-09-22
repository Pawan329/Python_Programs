
class Library:

    def borrowBook(self):
        library_file_read = open("Library.txt","r")
        library = library_file_read.readlines()
        updated_library = []

        if len(library) == 0:
            print("*** Sorry, No book available to bowrrow ***")

        elif len(library)>0:
            book_name = input("[Borrow] Please enter book name: ")
            book_name = book_name + "\n"

            if book_name in library:

                for book in library:
                    if book == book_name:
                        continue
                    else:
                        updated_library.append(book)
                
                library_file_read.close()
                open_library_txt = open("Library.txt","w")
                open_library_txt.writelines(updated_library)
                open_library_txt.close()

        
            else:
                print("*** Sorry, Required book is not available in library ***\n Press 'q' to QUIT")
                if book_name == "q\n": 
                    library_file_read.close()
                    Library.availableBooks(self)
                    return None

                else:
                    Library.borrowBook(self)


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