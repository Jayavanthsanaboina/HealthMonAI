import streamlit as st
import pandas as pd
import threading

from database import create_tables
from medication import add_medication,get_medications
from health_metrics import add_metrics,get_metrics
from chatbot import ask_health_question
from utils.reminder import start_reminder_service

create_tables()

threading.Thread(target=start_reminder_service, daemon=True).start()

st.title("Healthcare Monitoring AI Assistant")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Medication Tracker","Health Metrics","AI Chatbot"]
)

# Medication Tracker
if menu == "Medication Tracker":

    st.header("Medication Reminder")

    name = st.text_input("Medicine Name")
    time = st.text_input("Time (HH:MM)")

    if st.button("Add Medication"):
        add_medication(name,time)
        st.success("Medication Added")

    meds = get_medications()

    if meds:
        df = pd.DataFrame(meds,columns=["ID","Medicine","Time"])
        st.table(df)


# Health Metrics
elif menu == "Health Metrics":

    st.header("Health Tracking")

    steps = st.number_input("Steps Walked",0,50000)
    heart = st.number_input("Heart Rate",40,200)

    if st.button("Save Data"):
        add_metrics(steps,heart)
        st.success("Health Data Saved")

    data = get_metrics()

    if data:
        df = pd.DataFrame(data,columns=["ID","Steps","Heart Rate","Date"])
        st.table(df)


# AI Chatbot
else:

    st.header("AI Health Assistant")

    question = st.text_input("Ask a health question")

    if st.button("Ask AI"):

        if question:

            response = ask_health_question(question)

            st.write(response)