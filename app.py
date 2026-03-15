import streamlit as st
import matplotlib.pyplot as plt

from chatbot import ask_health_question
from health_metrics import calculate_bmi
from medication import add_new_medication, list_medications

st.title("HealthMonAI")

menu = st.sidebar.selectbox(
    "Menu",
    ["Chatbot","BMI Calculator","Medication Tracker","Health Report"]
)

# ---------------- CHATBOT ---------------- #

if menu == "Chatbot":

    question = st.text_input("Ask health question")

    if st.button("Ask"):
        response = ask_health_question(question)
        st.write(response)


# ---------------- BMI CALCULATOR ---------------- #

elif menu == "BMI Calculator":

    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")

    if st.button("Calculate BMI"):

        bmi = calculate_bmi(weight, height)

        st.write("Your BMI:", bmi)

        # BMI Visualization
        bmi_values = [18, 22, 25, 28, 30]

        fig, ax = plt.subplots()
        ax.plot(bmi_values, marker="o")
        ax.set_title("Sample BMI Trend")

        st.pyplot(fig)


# ---------------- MEDICATION TRACKER ---------------- #

elif menu == "Medication Tracker":

    name = st.text_input("Medicine Name")
    time = st.text_input("Time (HH:MM)")

    if st.button("Add Medication"):

        add_new_medication(name, time)
        st.success("Medication Added")

    if st.button("Show Medications"):

        meds = list_medications()
        st.table(meds)


# ---------------- HEALTH REPORT ---------------- #

elif menu == "Health Report":

    st.subheader("Simple Health Report")

    meds = list_medications()

    st.write("### Stored Medications")

    if meds:
        st.table(meds)
    else:
        st.write("No medications found")

    st.write("### Health Tips")
    st.write("• Maintain a healthy BMI")
    st.write("• Take medications on time")
    st.write("• Exercise regularly")

