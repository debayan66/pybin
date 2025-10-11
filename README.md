Library Management System (Python)

This is a console-based Library Management System implemented in Python using the pickle module for data storage. It allows users to add, view, search, modify, and delete book records efficiently without a database, making it lightweight and easy to use.

Features
1. Add Records

Add multiple books with details such as Book Number, Name, Author, Publisher, Quantity, and Price.

Saves all records in a binary file (library.dat) using pickle.

2. View Records

Display all books in a formatted tabular style.

3. Search Books

Search by Book Number, Book Name, or Author.

4. Quantity Check

Display books whose quantity is zero, helping to identify out-of-stock books.

5. Delete Records

Remove book entries safely from the library file.

6. Modify Records

Modify book details for a specific book.

Update prices (for example, adding a markup).
