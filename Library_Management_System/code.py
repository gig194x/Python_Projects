from collections import deque

# =====================
# Parent Class: LibraryItem
# =====================
class LibraryItem:
    def __init__(self, isbn, title, author):
        self.__isbn = isbn             # Private
        self.__title = title           # Private
        self.__author = author         # Private
        self.__available = True        # Private
        self.__waiting_list = deque()  # Private

    # ================= Getters =================
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def waiting_list_length(self):
        return len(self.__waiting_list)

    # ================= Methods =================
    def borrow(self, user):
        if self.__available:
            self.__available = False
            return True
        else:
            self.__waiting_list.append(user)
            return False

    def return_item(self):
        if self.__waiting_list:
            next_user = self.__waiting_list.popleft()
            return next_user
        else:
            self.__available = True
            return None

    # Polymorphism: override in subclasses
    def get_info(self):
        status = "Available" if self.__available else "Not Available"
        return f"[{self.__isbn}] {self.__title} by {self.__author} ({status})"


# =====================
# Subclass: Book
# =====================
class Book(LibraryItem):
    def get_info(self):
        return f"Book -> {super().get_info()}"


# =====================
# User Class
# =====================
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id          # Private
        self.__name = name                # Private
        self.__borrowed_books = []        # Private

    # Getters
    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def list_borrowed_books(self):
        return [b.get_title() for b in self.__borrowed_books]

    # Methods
    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)

    def has_book(self, book):
        return book in self.__borrowed_books


# =====================
# Library Class
# =====================
class Library:
    def __init__(self):
        self.__books = {}    # Private: ISBN -> Book
        self.__users = {}    # Private: user_id -> User
        self.__history = []  # Private: Stack for history

    # Add book
    def add_book(self, isbn, title, author):
        if isbn not in self.__books:
            self.__books[isbn] = Book(isbn, title, author)
            print(f"Book '{title}' added.")
        else:
            print("Book already exists.")

    # Remove book
    def remove_book(self, isbn):
        if isbn in self.__books:
            del self.__books[isbn]
            print(f"Book {isbn} removed.")
        else:
            print("Book not found.")

    # Search book
    def search_book(self, keyword):
        found = [b for b in self.__books.values() if keyword.lower() in b.get_title().lower()]
        if found:
            for b in found:
                print(b.get_info())
        else:
            print("No books found.")

    # Register user
    def register_user(self, user_id, name):
        if user_id not in self.__users:
            self.__users[user_id] = User(user_id, name)
            print(f"User '{name}' registered.")
        else:
            print("User already exists.")

    # Borrow book
    def borrow_book(self, user_id, isbn):
        if user_id not in self.__users:
            print("User not registered.")
            return
        if isbn not in self.__books:
            print("Book not found.")
            return

        user = self.__users[user_id]
        book = self.__books[isbn]

        if book.borrow(user):
            user.borrow_book(book)
            self.__history.append(f"{user.get_name()} borrowed '{book.get_title()}'")
            print(f"{user.get_name()} borrowed '{book.get_title()}'.")
        else:
            print(f"'{book.get_title()}' is not available. Added to waiting list.")

    # Return book
    def return_book(self, user_id, isbn):
        if user_id not in self.__users:
            print("User not registered.")
            return
        if isbn not in self.__books:
            print("Book not found.")
            return

        user = self.__users[user_id]
        book = self.__books[isbn]

        if user.has_book(book):
            next_user = book.return_item()
            user.return_book(book)
            self.__history.append(f"{user.get_name()} returned '{book.get_title()}'")
            print(f"{user.get_name()} returned '{book.get_title()}'.")

            if next_user:
                next_user.borrow_book(book)
                self.__history.append(f"{next_user.get_name()} borrowed '{book.get_title()}' from waiting list")
                print(f"{next_user.get_name()} borrowed '{book.get_title()}' (from waiting list).")
        else:
            print(f"{user.get_name()} does not have this book.")

    # View history
    def view_history(self):
        if self.__history:
            print("\n--- Library History ---")
            for action in reversed(self.__history):
                print(action)
        else:
            print("No history.")


# =====================
# Interactive Menu
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
