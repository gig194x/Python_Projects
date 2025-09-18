# Library Management System 
from collections import deque

# =====================
# Book Class
# =====================
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True
        self.waiting_list = deque()  # Queue of users waiting for this book

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"[{self.isbn}] {self.title} by {self.author} ({status})"


# =====================
# User Class
# =====================
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"User {self.user_id}: {self.name}"


# =====================
# Library Class
# =====================
class Library:
    def __init__(self):
        self.books = {}  # Dictionary {isbn: Book}
        self.users = {}  # Dictionary {id: User}
        self.history = []  # Stack of actions

    # -------- Book Management --------
    def add_book(self, isbn, title, author):
        if isbn not in self.books:
            self.books[isbn] = Book(isbn, title, author)
            print(f"Book '{title}' added to library.")
        else:
            print("Book already exists.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed.")
        else:
            print("Book not found.")

    def search_book(self, keyword):
        found = [book for book in self.books.values() if keyword.lower() in book.title.lower()]
        if found:
            for book in found:
                print(book)
        else:
            print("No books found.")

    # -------- User Management --------
    def register_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)
            print(f"User '{name}' registered successfully.")
        else:
            print("User already exists.")

    # -------- Borrow / Return --------
    def borrow_book(self, user_id, isbn):
        if user_id not in self.users:
            print("User not registered.")
            return
        if isbn not in self.books:
            print("Book not found.")
            return

        book = self.books[isbn]
        user = self.users[user_id]

        if book.available:
            book.available = False
            user.borrowed_books.append(book)
            self.history.append(f"{user.name} borrowed '{book.title}'")
            print(f"{user.name} borrowed '{book.title}'.")
        else:
            book.waiting_list.append(user)
            print(f"'{book.title}' is not available. {user.name} added to waiting list.")

    def return_book(self, user_id, isbn):
        if user_id not in self.users:
            print("User not registered.")
            return
        if isbn not in self.books:
            print("Book not found.")
            return

        book = self.books[isbn]
        user = self.users[user_id]

        if book in user.borrowed_books:
            user.borrowed_books.remove(book)
            self.history.append(f"{user.name} returned '{book.title}'")
            print(f"{user.name} returned '{book.title}'.")

            if book.waiting_list:
                next_user = book.waiting_list.popleft()
                next_user.borrowed_books.append(book)
                self.history.append(f"{next_user.name} borrowed '{book.title}' from waiting list")
                print(f"{next_user.name} borrowed '{book.title}' (from waiting list).")
            else:
                book.available = True
        else:
            print(f"{user.name} does not have this book.")

    # -------- History --------
    def view_history(self):
        if self.history:
            print("\n--- Library History ---")
            for action in reversed(self.history):  # Stack (LIFO)
                print(action)
        else:
            print("No history available.")


# =====================
# Main Program
# =====================
def main():
    library = Library()

    while True:
        print("\n==== Library Menu ====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Register User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View History")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(isbn, title, author)

        elif choice == "2":
            isbn = input("Enter ISBN to remove: ")
            library.remove_book(isbn)

        elif choice == "3":
            keyword = input("Enter title keyword to search: ")
            library.search_book(keyword)

        elif choice == "4":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            library.register_user(user_id, name)

        elif choice == "5":
            user_id = input("Enter User ID: ")
            isbn = input("Enter ISBN: ")
            library.borrow_book(user_id, isbn)

        elif choice == "6":
            user_id = input("Enter User ID: ")
            isbn = input("Enter ISBN: ")
            library.return_book(user_id, isbn)

        elif choice == "7":
            library.view_history()

        elif choice == "8":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

