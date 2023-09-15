#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(user='root', password='mk8328', host='127.0.0.1', database='lbms')
        if conn.is_connected():
            print("Connected to CSD LIBRARY ARENA, WELCOME")
            return conn
    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
    return None

def fetch_data():
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            roll_number = roll_number_entry.get()

            query = "SELECT rollno FROM lbms.studentsinfo;"
            cursor.execute(query)
            roll_numbers = [str(row[0]) for row in cursor]

            if roll_number in roll_numbers:
                book_name = book_name_entry.get()

                query = "SELECT bookname FROM lbms.booktable;"
                cursor.execute(query)
                book_names = [str(row[0]) for row in cursor]

                if book_name in book_names:
                    query = "SELECT qty FROM lbms.booktable WHERE bookname = %s;"
                    params = (book_name,)
                    cursor.execute(query, params)
                    qty = int(cursor.fetchone()[0])

                    updated_qty = qty - 1
                    update_query = "UPDATE booktable SET qty = %s WHERE bookname = %s;"
                    update_params = (updated_qty, book_name)
                    cursor.execute(update_query, update_params)
                    conn.commit()

                    output_label.config(text="Book quantity updated successfully.")
                else:
                    output_label.config(text="Invalid Book Name")
            else:
                output_label.config(text="Invalid Roll Number or You are not registered in the library")

            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print("Error executing query:", e)
    else:
        print("Not connected to the database")

# Create a tkinter window
window = tk.Tk()

# Create input fields
roll_number_label = tk.Label(window, text="Enter your roll number:")
roll_number_label.pack()
roll_number_entry = tk.Entry(window)
roll_number_entry.pack()

book_name_label = tk.Label(window, text="Enter the book name you need:")
book_name_label.pack()
book_name_entry = tk.Entry(window)
book_name_entry.pack()

# Create a button to trigger the update process
fetch_button = tk.Button(window, text="Fetch Data", command=fetch_data)
fetch_button.pack()

# Create an output label to display the result
output_label = tk.Label(window)
output_label.pack()

# Run the tkinter event loop
window.mainloop()


# In[ ]:




