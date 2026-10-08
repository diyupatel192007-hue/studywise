# 📚 StudyWise – Study Efficiency Predictor

> **A Machine Learning based web application that predicts a student's study efficiency based on their daily study habits and lifestyle factors.**

## 🌟 Overview

**StudyWise** is a simple Machine Learning web application designed to estimate a student's study efficiency using different academic and lifestyle factors.

The user enters information such as study hours, sleep hours, phone usage, breaks, exercise, focus level, stress level, and attendance. The trained Machine Learning model analyzes these inputs and predicts an estimated study efficiency score.

The project demonstrates how a Machine Learning model can be integrated into a real-world web application using Python and Flask.

---

## ✨ Features

* 📚 Study efficiency prediction
* 😴 Sleep and study habit analysis
* 📱 Phone usage consideration
* 🎯 Focus level input
* 😰 Stress level input
* 🏃 Exercise time consideration
* 🏫 Attendance consideration
* 🤖 Machine Learning based prediction
* 📊 Efficiency score from 0–100
* 🟢 High, Moderate, and Low efficiency classification
* 🌐 Simple and user-friendly web interface

---

## 🧠 How It Works

```text
Student Inputs
      ↓
Web Interface
      ↓
Flask Backend
      ↓
Machine Learning Model
      ↓
Efficiency Prediction
      ↓
Result Classification
      ↓
Result Display
```

The user provides their daily habits through the website. Flask receives the input and sends it to the trained Random Forest Regression model. The model predicts the study efficiency score, which is then displayed on the result page.

---

## 🤖 Machine Learning

The project uses **Random Forest Regression** to predict study efficiency.

### Input Features

| Feature        | Description                  |
| -------------- | ---------------------------- |
| Study Hours    | Hours spent studying per day |
| Sleep Hours    | Daily sleep duration         |
| Phone Hours    | Daily phone usage            |
| Breaks         | Number of study breaks       |
| Exercise Hours | Daily exercise duration      |
| Focus Level    | Focus level from 1–10        |
| Stress Level   | Stress level from 1–10       |
| Attendance     | Attendance percentage        |

### Target

**Efficiency Score**

The model predicts an estimated efficiency score between 0 and 100.

### Efficiency Categories

|  Score | Category               |
| -----: | ---------------------- |
| 75–100 | 🟢 High Efficiency     |
|  50–74 | 🟡 Moderate Efficiency |
|   0–49 | 🔴 Low Efficiency      |

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Random Forest Regression

### Data Processing

* Pandas
* NumPy

### Model Storage

* Joblib

---

## 📁 Project Structure

```text
StudyWise/
│
├── app.py
├── train_model.py
├── study_data.csv
├── model.pkl
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

### File Description

**app.py**
Flask application that handles user input and generates predictions.

**train_model.py**
Loads the dataset, trains the Machine Learning model, evaluates it, and saves the trained model.

**study_data.csv**
Dataset containing student study habits and efficiency values.

**model.pkl**
Trained Random Forest Regression model.

**index.html**
Main webpage where users enter their study information.

**result.html**
Displays the predicted study efficiency.

**style.css**
Contains the website styling.

**requirements.txt**
Contains the Python dependencies required to run the project.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/StudyWise.git
```

### 2. Open the project

```bash
cd StudyWise
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train_model.py
```

This generates:

```text
model.pkl
```

### 5. Run the Flask application

```bash
python app.py
```

### 6. Open in browser

Go to:

```text
http://127.0.0.1:5000
```

---

## 🖥️ Example Input

```text
Study Hours       : 6
Sleep Hours       : 8
Phone Usage       : 2
Breaks            : 3
Exercise Hours    : 1
Focus Level       : 8
Stress Level      : 3
Attendance        : 90%
```

### Example Output

```text
Study Efficiency: 80%

🟢 High Efficiency
```

*The actual prediction may vary depending on the trained model and dataset.*

---

## 📊 Model Evaluation

The Machine Learning model is evaluated using:

### Mean Absolute Error (MAE)

Measures the average difference between actual and predicted efficiency values.

### R² Score

Measures how well the model explains the variation in the target variable.

Run:

```bash
python train_model.py
```

to view the model's evaluation results.

---

## 🚀 Future Enhancements

* 📈 Interactive analytics dashboard
* 📊 More visualization features
* 👤 Student login and registration
* 💾 Prediction history
* 🎯 Personalized study recommendations
* 📅 Personalized study timetable
* 🧠 Comparison of multiple ML algorithms
* 📱 Improved mobile responsiveness
* 🗄️ Database integration
* 🌐 Cloud deployment

---

## ⚠️ Disclaimer

StudyWise is an educational Machine Learning project. The predicted efficiency score is an estimate based on the dataset and model used in the project.

It should not be considered a scientific or medical measurement of a student's actual academic performance.

---

## 🎓 Project Purpose

This project was developed as a college Machine Learning/Web Development project to demonstrate:

* Data preprocessing
* Machine Learning model training
* Model evaluation
* Model deployment in a web application
* Flask backend development
* HTML/CSS frontend development

---

## 👩‍💻 Author

**Diya Patel**

Student – Information Technology

---

## ⭐ Acknowledgement

This project helped demonstrate the practical integration of **Machine Learning with Web Development** and provided hands-on experience with Python, Flask, Pandas, Scikit-learn, HTML, and CSS.

---

## 📜 License

This project is created for educational and academic purposes.
