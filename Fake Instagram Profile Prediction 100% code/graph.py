import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk


root = tk.Tk()
root.configure(background="black")
root.geometry("1200x1450")
root.title("Login Form")

username = tk.StringVar()
password = tk.StringVar()

# For background Images
image1 = Image.open('graph.png').resize((360,260))
image2 = Image.open('Correlation.png').resize((360,260))
image3 = Image.open('bar.png').resize((360,260))
image4 = Image.open('grades.png').resize((360,260))

background_image1 = ImageTk.PhotoImage(image1)
background_image2 = ImageTk.PhotoImage(image2)
background_image3 = ImageTk.PhotoImage(image3)
background_image4 = ImageTk.PhotoImage(image4)

background_label1 = tk.Label(root, image=background_image1)
background_label1.image = background_image1
background_label1.place(x=100, y=20)

background_label2 = tk.Label(root, image=background_image2)
background_label2.image = background_image2
background_label2.place(x=600, y=20)

background_label3 = tk.Label(root, image=background_image3)
background_label3.image = background_image3
background_label3.place(x=100, y=400)

background_label4 = tk.Label(root, image=background_image4)
background_label4.image = background_image4
background_label4.place(x=600, y=400)


def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
    # Establish Connection
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

        # Find user If there is any take proper action
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                        "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()

        if result:
            ms.showinfo("Message", "Login successfully")
            from subprocess import call
            call(['python','Main.py'])
            root.destroy()
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

def Login():
    from subprocess import call
    call(["python", "GUI_main.py"])  

title = tk.Label(root, text="Accuracy Graph", font=("Algerian", 30, "bold", "italic"), bd=5, bg="black", fg="white")
# Adjusting the position of the label
title.place(x=400, y=300)

root.mainloop()

