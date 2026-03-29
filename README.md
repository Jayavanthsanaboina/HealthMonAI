# HealthMonAI
# HealthMonAI

HealthMonAI is an AI-powered healthcare monitoring assistant that helps users track fitness, manage medications, and receive general health guidance using an intelligent chatbot.

This project demonstrates a complete end-to-end healthcare monitoring system with AI integration and Indian healthcare features.

---

## Features

### AI Health Chatbot

* Ask general health-related questions
* Provides safe health advice
* Built using LangChain + Groq API

###  BMI Calculator (Fitness Tracking)

* Calculates Body Mass Index
* Displays BMI trend visualization

###  Medication Tracker

* Add and store medicines with time
* View stored medications using SQLite database

###  Medication Interaction Checker

* Detects possible interaction between two medicines

###  Health Data Visualization

* Displays BMI graph using matplotlib

###  Health Report Generation

* Shows stored medications
* Provides general health tips

###  JSON Data Handling

* Upload and view health data in JSON format

###  Health Goal Tracking

* Set personal health goals (e.g., target weight)

---

## 🇮🇳 Indian Healthcare Features (Week 5–6)

###  Indian Medicine Information

* Get details about common Indian medicines (e.g., Dolo 650, Crocin)

###  Indian Diet Recommendation

* Suggests diet plans based on goals (weight loss/gain/maintain)

###  Ayurvedic Suggestions

* Provides basic Ayurvedic remedies for common problems

---

##  Technologies Used

* Python
* Streamlit (User Interface)
* LangChain (AI Integration)
* Groq API (LLM)
* SQLite (Database)
* Matplotlib (Visualization)

---

##  Project Structure

```id="zndfd8"
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

##  How to Run the Project

1. Clone the repository

```id="iq8c7v"
git clone https://github.com/Jayavanthsanaboina/HealthMonAI.git
```

2. Navigate to the project folder

```id="k81w8r"
cd HealthMonAI
```

3. Install required libraries

```id="uh3xyl"
pip install streamlit langchain langchain-groq matplotlib
```

4. Add your API key in `chatbot.py`

```id="l3a7w2"
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY"
```

5. Run the application

```id="f3m8l2"
streamlit run app.py
```

---

##  Weekly Progress

### Week 1–2

* Project setup
* AI chatbot
* BMI calculator
* Medication tracker
* SQLite database

### Week 3–4

* Health tools integration
* BMI visualization
* Health report generation
* Medication interaction checking
* JSON data handling
* Goal tracking
* End-to-end workflow

### Week 5–6 (Half Completed)

* Indian medicine database
* Diet recommendation system
* Ayurvedic health suggestions
