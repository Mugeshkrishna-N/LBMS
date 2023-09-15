#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from mysql.connector import connection

def update_books():
    book_name = entry_book_name.get()
    quantity = int(entry_quantity.get())

    query = 'SELECT bookname FROM admintable;'
    cur.execute(query)
    book_names = [result[0] for result in cur.fetchall()]

    if book_name in book_names:
        values = (book_name, quantity)
        query = 'INSERT INTO booktable(bookname, qty) VALUES (%s, %s);'

        try:
            cur.execute(query, values)
            cnt.commit()
            print("Book updated successfully!")
        except Exception as e:
            print("Error inserting data:", e)
    else:
        print("Invalid book name")

# Create a MySQL connection
cnt = connection.MySQLConnection(user='root', password='mk8328', host='127.0.0.1', database='lbms')

if cnt.is_connected() == False:
    print("Not connected ")
else:
    print("Connected to CSD LIBRARY ARENA, WELCOME ")
cur = cnt.cursor()

# Create the main window
window = tk.Tk()
window.title("Library Management System")

# Create a label for book name
label_book_name = tk.Label(window, text="Enter the book name:")
label_book_name.pack()

# Create an entry field for book name
entry_book_name = tk.Entry(window)
entry_book_name.pack()

# Create a label for quantity
label_quantity = tk.Label(window, text="Enter the quantity:")
label_quantity.pack()

# Create an entry field for quantity
entry_quantity = tk.Entry(window)
entry_quantity.pack()

# Create a button to update books
update_books_button = tk.Button(window, text="Update Books", command=update_books)
update_books_button.pack()

# Start the main event loop
window.mainloop()


# In[ ]:




