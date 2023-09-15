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

def fetch_data_from_database():
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM booktable'
            cursor.execute(query)
            result = ""
            for row in cursor:
                for item in row:
                    result += str(item) + " "
                result += "\n"
            text_area.insert(tk.END, result)
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print("Error executing query:", e)
    else:
        print("Not connected to the database")

# Create a tkinter window
window = tk.Tk()

# Create a text widget for output
text_area = tk.Text(window)
text_area.pack()

# Create a button to fetch data
fetch_button = tk.Button(window, text="Fetch Data", command=fetch_data_from_database)
fetch_button.pack()

# Run the tkinter event loop
window.mainloop()


# In[ ]:




