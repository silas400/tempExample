import sqlite3


conn = sqlite3.connect("Books.db")
cursor = conn.cursor()

datalist = []
Book = []

command = input("add (Title) (Quantity) (Author) / read: ")
if command == "read":
    dataencrypted = cursor.execute("SELECT * FROM Books")
    for x in dataencrypted.fetchall():
        Book.append("Title: " + x[0])
        Book.append("Quantity: " + str(x[1]))
        Book.append("Author: " + x[2])
        print(Book)
        Book = []
if command.split()[0] == 'add':
    title = input("Title: ")
    quantity = input("Quantity: ")
    author = input("Author: ")
    cursor.execute("INSERT INTO Books (Title, Quantity, Author) VALUES (?, ?, ?)", (title, quantity, author,))
if command == "shift":
    quantity = 0
    Book = input("Book title?: ")
    dataencrypted = cursor.execute("SELECT * FROM Books")
    for x in dataencrypted.fetchall():
        if x[0] == Book:
            quantity = x[1]
            print(x)
    shiftType = input("increase or decrease?: ")
    if shiftType == "increase":
        number = int(input("Amount: "))
        result = int(quantity) + number
        cursor.execute("UPDATE Books SET Quantity = (?) WHERE Title = (?)", (result, Book))
    if shiftType == "decrease":
        number = int(input("Amount: "))
        result = int(quantity) - number
        cursor.execute("UPDATE Books SET Quantity = (?) WHERE Title = (?)", (result, Book))


conn.commit()
conn.close()