class Book:
    def __init__(self,book_id,title,author,available_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available_copies= available_copies
        
    def display_book_details(self):
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Available Copies: {self.__available_copies}")
    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"'{self.__title}' borrowed successfully. {self.__available_copies} copies remaining.")
            return True
        else:
            print(f"'{self.__title}' is currently out of stock.")
            return False
    def return_book(self):
        self.__available_copies += 1
        print(f"'{self.__title}' returned successfully. {self.__available_copies} copies available.")
        
    def get_title(self):
        return self.__title

    def get_book_id(self):
        return self.__book_id
class Library:
    def __init__(self):
        self.__books = []
    def add_new_book(self,book):
        self.__books.append(book)
        # print(f"Book '{book.get_title()}' added to the library.")
    def search_for_book_by_title(self,title):
        found_books = [book for book in self.__books if title.lower() in book.get_title().lower()]
        if found_books:
            print("\n found books:")
            for book in found_books:
                book.dispalay_book_details()
            else:
                print(f"No books found with title containing '{title}'.")
            return found_books
    def display_all_books(self):
        if not self.__books:
            print("The library currently has no books.")
            return
        print("\n--- All Books in Library ---")
        for book in self.__books:
            book.display_book_details()
            print("-" * 20)
    def find_book_by_id(self, book_id):
        for book in self.__books:
            if book.get_book_id() == book_id:
                return book
        return None

library = Library()
book1 = Book(101, "The Great Gatsby", "F. Scott Fitzgerald", 3)
book2 = Book(102, "To Kill a Mockingbird", "Harper Lee", 5)
book3 = Book(103, "1984", "George Orwell", 2)

library.add_new_book(book1)
library.add_new_book(book2)
library.add_new_book(book3)

while True:
        print("\n--- Library Management System Menu ---")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search a book by title")
        print("5. Exit")
        
        
        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_all_books()
        elif choice == '2':
            book_id = int(input("Enter the Book ID to borrow: "))
            book = library.find_book_by_id(book_id)
            if book:
                book.borrow_book()
            else:
                print("Book not found.")
        elif choice == '3':
            book_id = int(input("Enter the Book ID to return: "))
            book = library.find_book_by_id(book_id)
            if book:
                book.return_book()
            else:
                print("Book not found.")
        elif choice == '4':
            title_search = input("Enter the title (or part of it) to search: ")
            library.search_for_book_by_title(title_search)
        elif choice == '5':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        

        