# HealthMonAI
# HealthMonAI

HealthMonAI is an AI-powered healthcare monitoring assistant that helps users track health metrics, manage medications, and receive basic health guidance through an AI chatbot.

This project demonstrates how artificial intelligence can assist in everyday health monitoring and encourage healthier lifestyles.

---

## Project Features

### 1. AI Health Chatbot

* Users can ask general health-related questions.
* The chatbot provides safe health advice.
* Built using LangChain with Groq LLM integration.

### 2. BMI Calculator (Fitness Tracking)

* Users can enter weight and height.
* The system calculates Body Mass Index (BMI).
* Provides a simple visualization of BMI trends.

### 3. Medication Tracker

* Users can store medication names and scheduled times.
* Stored data can be viewed later.
* Uses SQLite database for persistent storage.

### 4. Health Data Visualization

* Displays a sample BMI trend graph using matplotlib.

### 5. Simple Health Report

* Shows stored medications.
* Provides general health recommendations.

---

## Technologies Used

* Python
* Streamlit (User Interface)
* LangChain (AI integration)
* Groq API (LLM inference)
* SQLite (Database)
* Matplotlib (Data visualization)

---

## Project Structure

```
healthmonai
│
├── app.py                # Main Streamlit application
├── chatbot.py            # AI health chatbot using LangChain
├── health_metrics.py     # BMI calculation functions
├── medication.py         # Medication management logic
├── database.py           # SQLite database setup
└── utils/
    └── reminder.py       # Medication reminder service
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/Jayavanthsanaboina/HealthMonAI.git
```

2. Navigate to the project folder

```
cd HealthMonAI
```

3. Install required libraries

```
pip install streamlit langchain langchain-groq matplotlib
```

4. Add your Groq API key in `chatbot.py`

```
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY"
```

5. Run the application

```
streamlit run app.py
```

---

## Weekly Progress

### Week 1–2

* Project setup
* AI chatbot implementation
* BMI calculator
* Medication tracker
* SQLite database integration

### Week 3–4 (Partial)

* Integrated health tools
* BMI data visualization
* Simple health report generation
