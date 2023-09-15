#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')
import tkinter as tk
from mysql.connector import connection

def add_book():
    admin_id = int(entry_admin_id.get())
    password = entry_password.get()

    query = 'SELECT * FROM lbms.admininfo;'
    cur.execute(query)
    admin_info = cur.fetchall()
    print(admin_info)
    admin_passwords = [info[2] for info in admin_info]
    print(admin_passwords)

    if password in admin_passwords:
        admin_name = entry_admin_name.get()
        book_name = entry_book_name.get()
        author = entry_author.get()
        category = entry_category.get()
        place = entry_place.get()

        query = 'INSERT INTO lbms.admintable(adminname, adminid, bookname, authorname, category, place) VALUES (%s, %s, %s, %s, %s, %s);'
        values = (admin_name, admin_id, book_name, author, category, place)

        try:
            cur.execute(query, values)
            cnt.commit()
            print("Book added successfully!")
        except Exception as e:
            print("Error inserting data:", e)
    else:
        print("Invalid admin password ")

# Create a MySQL connection
cnt = connection.MySQLConnection(user='root', password='mk8328', host='127.0.0.1', database='lbms')

if cnt.is_connected() == False:
    print("Not connected ")
else:
    print("Connected to CSD LIBRARY ARENA, WELCOME ")
cur = cnt.cursor()
curs=cnt.cursor()

# Create the main window
window = tk.Tk()
window.title("Library Management System")

# Create a label for admin ID
label_admin_id = tk.Label(window, text="Enter your admin ID:")
label_admin_id.pack()

# Create an entry field for admin ID
entry_admin_id = tk.Entry(window)
entry_admin_id.pack()

# Create a label for password
label_password = tk.Label(window, text="Enter your password:")
label_password.pack()

# Create an entry field for password
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create a label for admin name
label_admin_name = tk.Label(window, text="Enter your name:")
label_admin_name.pack()

# Create an entry field for admin name
entry_admin_name = tk.Entry(window)
entry_admin_name.pack()

# Create a label for book name
label_book_name = tk.Label(window, text="Enter the book name:")
label_book_name.pack()

# Create an entry field for book name
entry_book_name = tk.Entry(window)
entry_book_name.pack()

# Create a label for author
label_author = tk.Label(window, text="Enter the author:")
label_author.pack()

# Create an entry field for author
entry_author = tk.Entry(window)
entry_author.pack()

# Create a label for category
label_category = tk.Label(window, text="Enter the category:")
label_category.pack()

# Create an entry field for category
entry_category = tk.Entry(window)
entry_category.pack()

# Create a label for place
label_place = tk.Label(window, text="Enter the place:")
label_place.pack()

# Create an entry field for place
entry_place = tk.Entry(window)
entry_place.pack()

# Create a button to add a book
add_book_button = tk.Button(window, text="Add Book", command=add_book)
add_book_button.pack()

# Start the main event loop
window.mainloop()


# In[ ]:




