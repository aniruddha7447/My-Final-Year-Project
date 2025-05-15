import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="Brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Towards Safer Online Spaces:\n Detection of Unsafe Youth Conversations on Instagram")

# 44

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('09.jpg')
image2 = image2.resize((1800,700))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=10, y=10)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Towards Safer Online Spaces:\n Detection of Unsafe Youth Conversations on Instagram",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="#ffb366", width=50, height=2)
label_l1.place(x=50, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

# def reg():
#     from subprocess import call
#     call(["python","registration.py"])

# def log():
#     from subprocess import call
#     call(["python","login.py"])
    
def window():
  root.destroy()


# button1 = tk.Button(root, text="Login", command=log, width=15, height=1,font=('times', 20, ' bold '), bg="#f261cf", fg="#001a1a")
# button1.place(x=10, y=280)

# button2 = tk.Button(root, text="Register",command=reg,width=15, height=1,font=('times', 20, ' bold '), bg="#f261cf", fg="black")
# button2.place(x=75, y=340)

button3 = tk.Button(root, text="Dataset",command=window,width=15, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button3.place(x=200, y=200)

root.mainloop()