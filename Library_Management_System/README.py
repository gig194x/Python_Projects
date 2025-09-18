# 📚 Library Management System

Mini-project in **Python** applying **Object-Oriented Programming (OOP)** and common **Data Structures**.

---

## 🎯 Features

* **OOP Classes**:

  * `Book` → holds book details (title, author, ISBN, availability).
  * `User` → manages user info and borrowed books.
  * `Library` → core system (books, reservations, history).

* **Data Structures**:

  * **Dictionary** → store books by ISBN for quick lookup.
  * **Queue (deque)** → manage waiting list for reserved books.
  * **Stack (list)** → track last borrow/return actions (history).

---

## 🛠️ Functions

* Add new books to the library.
* Register users.
* Borrow and return books.
* View reservation queue.
* Check borrow/return history.

---

## 🚀 Tech

* Language: **Python 3**
* Built-in Data Structures: `dict`, `deque`, `list`.

---

## 📌 Example Use Cases

* User borrows a book → added to history (stack).
* If unavailable → added to reservation queue.
* Admin can check current books & past transactions.

---



