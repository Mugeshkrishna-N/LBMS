#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from mysql.connector import connection

def insert_student_info():
    student_name = entry_student_name.get()
    roll_number = entry_roll_number.get()

    query = 'INSERT INTO studentsinfo (studentname, rollno) VALUES (%s, %s);'
    values = (student_name, roll_number)

    try:
        cur.execute(query, values)
        cnt.commit()
        print("Student information inserted successfully!")
    except Exception as e:
        print("Error inserting data:", e)

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

# Create a label for student name
label_student_name = tk.Label(window, text="Enter the student name:")
label_student_name.pack()

# Create an entry field for student name
entry_student_name = tk.Entry(window)
entry_student_name.pack()

# Create a label for roll number
label_roll_number = tk.Label(window, text="Enter the roll number:")
label_roll_number.pack()

# Create an entry field for roll number
entry_roll_number = tk.Entry(window)
entry_roll_number.pack()

# Create a button to insert student information
insert_info_button = tk.Button(window, text="Insert Student Info", command=insert_student_info)
insert_info_button.pack()

# Start the main event loop
window.mainloop()


# In[ ]:





# In[ ]:




