#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from mysql.connector import connection

def create_admin_profile():
    print("Enter your faculty password to confirm you are a faculty ")
    s = entry_password.get()
    if s == 'faculty':
        print("Enter your name ")
        ana = entry_name.get()
        print("Enter your id no ")
        aid = int(entry_id.get())
        print("Enter your new password ")
        apa = entry_new_password.get()
        q = 'insert into lbms.admininfo(adminname, adminid, password) values (%s, %s, %s);'
        t = (ana, aid, apa)
        try:
            cur.execute(q, t)
            cnt.commit()
            print("Admin profile created successfully!")
        except Exception as e:
            print("Error inserting data:", e)
    else:
        print("Invalid faculty password ")


cnt = connection.MySQLConnection(user='root', password='mk8328', host='127.0.0.1', database='lbms')

if cnt.is_connected() == False:
    print("Not connected ")
else:
    print("Connected to CSD LIBRARY ARENA, WELCOME ")
cur = cnt.cursor()

window = tk.Tk()
window.title("Library Management System")

label_password = tk.Label(window, text="Enter your faculty password:")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

label_name = tk.Label(window, text="Enter your name:")
label_name.pack()

entry_name = tk.Entry(window)
entry_name.pack()

label_id = tk.Label(window, text="Enter your ID number:")
label_id.pack()

entry_id = tk.Entry(window)
entry_id.pack()

label_new_password = tk.Label(window, text="Enter your new password:")
label_new_password.pack()

entry_new_password = tk.Entry(window, show="*")
entry_new_password.pack()

create_profile_button = tk.Button(window, text="Create Admin Profile", command=create_admin_profile)
create_profile_button.pack()

window.mainloop()


# In[ ]:





# In[ ]:




