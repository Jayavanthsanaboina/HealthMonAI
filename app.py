import streamlit as st
import matplotlib.pyplot as plt
import json

from chatbot import ask_health_question
from health_metrics import calculate_bmi
from medication import add_new_medication, list_medications, check_interaction, get_medicine_info

st.title("HealthMonAI - AI Healthcare Assistant")

menu = st.sidebar.selectbox(
    "Menu",
    ["Chatbot","BMI Calculator","Medication Tracker","Health Report","Extra Features","Indian Health Features"]
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
        ax.set_title("BMI Trend")
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

    st.subheader("Medicine Info")

    med = st.text_input("Enter medicine name")

    if st.button("Get Info"):
        st.write(get_medicine_info(med))


# ---------------- HEALTH REPORT ---------------- #
elif menu == "Health Report":

    st.write("### Medications")
    st.table(list_medications())

    st.write("### Health Tips")
    st.write("Maintain healthy lifestyle")
    st.write("Exercise regularly")
    st.write("Take medicines on time")


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


# ---------------- INDIAN HEALTH FEATURES ---------------- #
elif menu == "Indian Health Features":

    # Diet Recommendation
    st.subheader("Indian Diet Suggestion")

    diet = st.selectbox("Select Goal", ["Weight Loss", "Weight Gain", "Maintain"])

    if st.button("Get Diet Plan"):

        if diet == "Weight Loss":
            st.write("Eat roti, vegetables, dal, avoid fried food")

        elif diet == "Weight Gain":
            st.write("Include rice, milk, nuts, banana")

        else:
            st.write("Balanced diet with roti, rice, dal, vegetables")

    # Ayurvedic Advice
    st.subheader("Ayurvedic Suggestions")

    problem = st.text_input("Enter health issue")

    if st.button("Get Ayurvedic Advice"):

        if "cold" in problem.lower():
            st.write("Try turmeric milk and ginger tea")

        elif "digestion" in problem.lower():
            st.write("Use jeera water and triphala")

        else:
            st.write("Consult Ayurvedic doctor")
