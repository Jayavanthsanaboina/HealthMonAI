# HealthMonAI
# HealthMonAI

HealthMonAI is an AI-powered healthcare monitoring assistant that helps users track fitness, manage medications, and receive general health guidance through an intelligent chatbot.

This project provides a complete end-to-end healthcare workflow with a professional interface and Indian healthcare support features.

---

## 🚀 Features

### 🤖 AI Health Chatbot

* Ask general health-related questions
* Provides safe and basic health advice
* Includes error handling for API failures

### 🏃 BMI Calculator

* Calculates Body Mass Index (BMI)
* Displays BMI trend visualization using graphs
* Includes input validation for accurate results

### 💊 Medication Tracker

* Add and store medicines with time
* View stored medications
* Check medicine interactions
* Get basic medicine information

### 📊 Health Dashboard

* Displays key health metrics
* Shows BMI and goal tracking
* Provides a quick overview of user health

### 📄 Health Report

* Displays stored medications
* Provides general health tips
* Export report as CSV file

### 📁 Data Handling

* Upload and display JSON health data
* Supports multiple data formats

### 🎯 Health Goal Tracking

* Set personal health goals (e.g., target weight)

---

## 🇮🇳 Indian Healthcare Features

### 💊 Medicine Information

* Get details about common Indian medicines

### 🥗 Diet Recommendation

* Suggests diet plans for weight loss, gain, or maintenance

### 🌿 Ayurvedic Suggestions

* Provides natural remedies for common problems

### 🩺 Doctor Suggestion System

* Suggests doctors based on city
* Implemented using a local database (simulated API)

### 📋 Medical History

* Allows users to input and store basic medical history

### 🛡 Insurance Support

* Basic insurance awareness feature

### 🌍 Regional Preferences

* Suggests diet based on region

---

## 🛠 Technologies Used

* Python
* Streamlit
* LangChain
* Groq API
* SQLite
* Matplotlib
* Pandas

---

## 📁 Project Structure

```
healthmonai
│
├── app.py
├── chatbot.py
├── health_metrics.py
├── medication.py
├── database.py
└── utils/
    └── reminder.py
```

---

## ▶ How to Run the Project

1. Clone the repository

```
git clone https://github.com/Jayavanthsanaboina/HealthMonAI.git
```

2. Navigate to project folder

```
cd HealthMonAI
```

3. Install dependencies

```
pip install streamlit langchain langchain-groq matplotlib pandas
```

4. Add API key in chatbot.py

```
os.environ["GROQ_API_KEY"] = "YOUR_API_KEY"
```

5. Run the application

```
streamlit run app.py
```

---

## 📅 Weekly Progress

### Week 1–2

* Project setup
* AI chatbot
* BMI calculator
* Medication tracker
* Database integration

### Week 3–4

* Health tools integration
* Data visualization
* Health report generation
* Medication interaction checking
* JSON handling
* Goal tracking

### Week 5–6

* Indian healthcare features
* Diet recommendation
* Ayurvedic suggestions
* Doctor system (local database)
* Medical history
* Insurance support

### Week 7–8

* Professional dashboard
* Input validation
* Error handling
* Export functionality (CSV)
* UI improvements
* Production-ready application

---

## 🎬 Demo Video

The demo video (5–7 minutes) showcases:

* Dashboard overview
* Chatbot interaction
* BMI calculation with graph
* Medication tracking
* Report export
* Indian healthcare features

---
