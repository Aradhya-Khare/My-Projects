class Library:
    
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def avialableBooks(self):
        print("The available books are:")
        for book in self.books:
            print("*" + book)    

    def borrowBook(self,Bookname):
        if Bookname in self.books:
            print(f"You have been assigned {Bookname} kindly please return it in 30 days")
            self.books.remove(Bookname)
        else:
            print("The book is not availble curently")

    def returnBook(self, Bookname):
        self.books.append(Bookname)
        print("Thanks for returning the book")


class Student:
    
    def requestBook(self):
        self.book = input("Which book you want from the library: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Which book you want return to the library: ")
        return self.book
    
centrlLibrary = Library(["Science", "Maths", "Social Studies", "English"])
student = Student()
while(True):
    wel = '''Welcome to the central library
    Please select an option
    1. Show list of available books
    2. Request a book
    3. Return a book
    4. Exit the library
    '''
    print(wel)

    a = int(input("Enter your selected opption"))
    
    if a == 1:
        centrlLibrary.avialableBooks()
    elif a == 2:
        centrlLibrary.borrowBook(student.requestBook())
    elif a == 3:
        centrlLibrary.returnBook(student.returnBook())
    elif a == 4:
        print("Thank you for using this library")
        exit()
    else:
        print("Invalid Imput")