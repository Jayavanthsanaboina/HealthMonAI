# 🏥 HealthMonAI

HealthMonAI is an AI-powered healthcare assistant developed using **Python**, **Streamlit**, **LangChain**, **Groq LLM**, and **SQLite**. The application helps users monitor their health, calculate BMI, manage medications, generate personalized health reports, and receive AI-assisted healthcare guidance.

---

## 🚀 Features

### 🤖 AI Healthcare Chatbot
- Ask general health-related questions
- Safe AI-generated healthcare guidance
- Encourages consulting healthcare professionals for serious conditions

### 📊 BMI Calculator
- Calculates Body Mass Index (BMI)
- Displays BMI category
- Health visualization using charts
- Water intake recommendation
- Health score estimation

### 💊 Medication Center
- Add medications
- View medication history
- Check common medicine interactions
- Medication reminders
- Medicine information using AI

### 📄 Health Report
- Medication summary
- AI-generated daily health tips
- Health progress overview

### 🎯 Health Goals
- Set personal health goals
- Track target weight
- Monitor progress

### 🇮🇳 Indian Healthcare Features
- AI-powered Indian Diet Planner
- AI Ayurvedic Assistant
- AI Doctor Recommendation
- Health Insurance Guidance

---

## 🛠 Technologies Used

- Python
- Streamlit
- LangChain
- Groq LLM
- SQLite
- Matplotlib
- Pandas

---

## 📂 Project Structure

```
HealthMonAI/
│
├── .streamlit/
│   └── secrets.toml
│
├── data/
│   └── health.db
│
├── utils/
│   ├── __init__.py
│   └── reminder.py
│
├── app.py
├── chatbot.py
├── database.py
├── medication.py
├── health_metrics.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/HealthMonAI.git
```

Move into the project folder

```bash
cd HealthMonAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a file named

```
.streamlit/secrets.toml
```

Add your Groq API Key

```toml
GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Modules

- AI Health Chatbot
- BMI Calculator
- Medication Tracker
- Health Dashboard
- Health Reports
- Goal Tracker
- Indian Healthcare Services

---

## 📸 Screenshots

You can add screenshots here after deployment.

Example:

- Dashboard
- AI Chatbot
- Medication Center
- BMI Calculator
- Health Reports
- Indian Healthcare

---

## 🔮 Future Enhancements

- Integration with wearable devices
- Appointment booking system
- Cloud database support
- Electronic Health Records (EHR)
- Voice-enabled AI assistant
- Email and SMS medication reminders

---

## 👨‍💻 Developer

**Sanaboina Satya Jayavanth**

HealthMonAI – AI Powered Healthcare Assistant

---

## 📄 License

This project is developed for educational purposes.
