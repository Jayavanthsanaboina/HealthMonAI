import streamlit as st
import matplotlib.pyplot as plt
import json

from chatbot import ask_health_question
from health_metrics import calculate_bmi
from medication import add_new_medication, list_medications, check_interaction

st.title("HealthMonAI")

menu = st.sidebar.selectbox(
    "Menu",
    ["Chatbot","BMI Calculator","Medication Tracker","Health Report","Extra Features"]
)

# ---------------- CHATBOT ---------------- #
if menu == "Chatbot":

    q = st.text_input("Ask health question")

    if st.button("Ask"):
        st.write(ask_health_question(q))


# ---------------- BMI ---------------- #
elif menu == "BMI Calculator":

    w = st.number_input("Weight (kg)")
    h = st.number_input("Height (cm)")

    if st.button("Calculate"):
        bmi = calculate_bmi(w, h)
        st.write("BMI:", bmi)

        # Visualization
        bmi_values = [18, 22, 25, 28, 30]
        fig, ax = plt.subplots()
        ax.plot(bmi_values)
        st.pyplot(fig)


# ---------------- MEDICATION ---------------- #
elif menu == "Medication Tracker":

    name = st.text_input("Medicine")
    time = st.text_input("Time")

    if st.button("Add"):
        add_new_medication(name, time)
        st.success("Added")

    if st.button("Show"):
        st.table(list_medications())

    st.subheader("Check Interaction")

    m1 = st.text_input("Medicine 1")
    m2 = st.text_input("Medicine 2")

    if st.button("Check"):
        st.write(check_interaction(m1, m2))


# ---------------- HEALTH REPORT ---------------- #
elif menu == "Health Report":

    st.write("### Medications")
    st.table(list_medications())

    st.write("### Tips")
    st.write("Maintain healthy lifestyle")


# ---------------- EXTRA FEATURES ---------------- #
elif menu == "Extra Features":

    # JSON Upload
    st.subheader("Upload JSON Data")

    file = st.file_uploader("Upload JSON", type="json")

    if file:
        data = json.load(file)
        st.write(data)

    # Goal Setting
    st.subheader("Set Health Goal")

    goal = st.number_input("Target Weight")

    if st.button("Save Goal"):
        st.success(f"Goal saved: {goal} kg")
