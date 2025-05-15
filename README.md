# Fake Instagram Profile Identification and Classification Using Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![University](https://img.shields.io/badge/University-SPPU-blue)
![Status](https://img.shields.io/badge/Project-Completed-success)

A GUI-based Python project to identify and classify **fake Instagram profiles** using machine learning algorithms like **SVM**, **Decision Tree**, and **Random Forest**. This desktop tool includes user authentication, real-time predictions, and rich visualizations — all in an intuitive interface.

---

## 🎞️ Live Demo

> 💡 *Include this GIF in your repo under `screenshots/demo.gif` or change the path.*

![Demo](screenshots/demo.gif)

---

## ✅ Key Features

- 🧠 Predicts **Fake** or **Not Fake** using trained ML models  
- 🔐 Login and registration with **SQLite** database  
- 📊 Visual insights with **graphs and accuracy comparison**  
- 🖥️ Intuitive **Tkinter-based GUI**  
- 💾 Models saved using `joblib` for reuse

---

## 💡 Technologies Used

| Category         | Tech Stack                      |
|------------------|----------------------------------|
| Programming      | Python 3                         |
| GUI              | Tkinter                          |
| ML Algorithms    | SVM, Random Forest, Decision Tree|
| Data Processing  | Pandas, NumPy                    |
| Visualization    | Matplotlib, Seaborn              |
| Image Support    | Pillow (PIL)                     |
| Database         | SQLite                           |

---

## 📁 Project Structure

BE Project/
│
├── codes/
│ ├── GUI_main.py # Main app file
│ ├── Model_SVM.py # SVM training
│ ├── Model_RF.py # Random Forest training
│ ├── Model_DT.py # Decision Tree training
│ ├── Prediction.py # Prediction form logic
│ ├── Register.py # User registration
│ ├── Login.py # User login
│ ├── Graph.py # Accuracy graph UI
│ ├── utils/ # Support modules
│ └── ss/ # Screenshots folder
│
├── datasets/ # Dataset files
├── Report/ # Project documentation
├── PPT/ # Final presentation slides
└── README.md


---

## 🖼 Screenshots

> 📌 *Place your screenshots in `screenshots/` folder or update the paths.*

### 🔐 Login Page  
![Login](screenshots/login.png)

### 📝 Register Page  
![Register](screenshots/register.png)

### 📊 Accuracy Graph  
![Graph](screenshots/graph.png)

### 🧾 Prediction Input  
![Input](screenshots/input.png)

### ✅ Prediction Output  
![Result](screenshots/result.png)

---

## ▶️ How It Works

1. Run `GUI_main.py`  
2. Register or Login  
3. Train model (SVM, DT, RF)  
4. Input Instagram profile data  
5. Get prediction result  
6. View accuracy graphs and model comparison

---

## 👨‍💻 Developed By

🎓 **Savitribai Phule Pune University**  
👩‍🏫 *Project Guide:* Prof. Priyanka Kinage  

**Team Members:**
- Apurv Badave  
- Aniruddha Lalge  
- Nikhil Elajale  
- Pankaj Godara
