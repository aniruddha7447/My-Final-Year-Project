
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump


root = tk.Tk()
root.title("Fake Instagram Profile Prediction Using Machine Learning")
root.configure(background="purple")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image = Image.open('s4.jpg')
image = image.resize((w, h))
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=100, y=0)

lbl = tk.Label(root, text="Fake Instagram Profile Prediction Using Machine Learning", font=('times', 35,' bold '), height=1, width=62, bg="purple", fg="white")
lbl.place(x=0, y=0)


def Model_Training():
    data = pd.read_csv("C:\BE Project\Fake Instagram Profile Prediction 100% code\insta_test.csv").dropna()
    x = data.drop(['fake'], axis=1)
    y = data['fake']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=12)
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)
    y_pred = svcclassifier.predict(x_test)
    repo = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred) * 100
    
    label4 = tk.Label(root, text=str(repo), width=45, height=10, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=305, y=200)
    
    label5 = tk.Label(root, text="Accuracy: %.2f%%\nModel saved as svm.joblib" % accuracy, width=45, height=3, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label5.place(x=305, y=420)
    
    dump(svcclassifier, "svm.joblib")
    print("Model saved as svm.joblib")


def Model_Training1():
    data = pd.read_csv("C:\BE Project\Fake Instagram Profile Prediction 100% code\insta_test.csv").dropna()
    x = data.drop(['fake'], axis=1)
    y = data['fake']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=111)
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=123)
    rf_classifier.fit(x_train, y_train)
    y_pred = rf_classifier.predict(x_test)
    repo = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred) * 100
    
    label4 = tk.Label(root, text=str(repo), width=45, height=10, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=305, y=200)
    
    label5 = tk.Label(root, text="Accuracy: %.2f%%\nModel saved as random_forest.joblib" % accuracy, width=45, height=3, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label5.place(x=305, y=420)
    
    dump(rf_classifier, "random_forest.joblib")
    print("Model saved as random_forest.joblib")


def Model_Training2():
    data = pd.read_csv("C:\BE Project\Fake Instagram Profile Prediction 100% code\insta_test.csv").dropna()
    x = data.drop(['fake'], axis=1)
    y = data['fake']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=12)
    dt_classifier = DecisionTreeClassifier(random_state=42)
    dt_classifier.fit(x_train, y_train)
    y_pred = dt_classifier.predict(x_test)
    repo = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred) * 100
    
    label4 = tk.Label(root, text=str(repo), width=45, height=10, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=305, y=200)
    
    label5 = tk.Label(root, text="Accuracy: %.2f%%\nModel saved as decision_tree.joblib" % accuracy, width=45, height=3, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label5.place(x=305, y=420)
    
    dump(dt_classifier, "decision_tree.joblib")
    print("Model saved as decision_tree.joblib")


def call_file():
   from subprocess import call
   call(['python','Check.py'])


def window():
    root.destroy()


button3 = tk.Button(root, foreground="white", background="#152238", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_SVM", command=Model_Training, width=15, height=2)
button3.place(x=5, y=200)

button5 = tk.Button(root, foreground="white", background="#152238", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_RF", command=Model_Training1, width=15, height=2)
button5.place(x=5, y=300)

button6 = tk.Button(root, foreground="white", background="#152238", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model_DT", command=Model_Training2, width=15, height=2)
button6.place(x=5, y=400)

button4 = tk.Button(root, foreground="white", background="#152238", font=("Tempus Sans ITC", 14, "bold"),
                    text="Check", command=call_file, width=15, height=2)
button4.place(x=5, y=500)

exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=600)

root.mainloop()

