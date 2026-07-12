import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import json
from datetime import datetime

from chatbot import ask_health_question
from health_metrics import (
    calculate_bmi,
    bmi_category,
    daily_water_intake,
    calorie_estimate,
    health_score
)
from medication import (
    add_new_medication,
    list_medications,
    check_interaction
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="HealthMonAI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- HEADER ---------------- #

st.title("🏥 HealthMonAI")
st.caption("AI-Powered Personal Healthcare Assistant")
st.markdown("---")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🏥 HealthMonAI")

st.sidebar.markdown("### Navigation")

menu = st.sidebar.radio(
    "",
    [
        "🏠 Dashboard",
        "🤖 AI Chatbot",
        "📊 BMI Calculator",
        "💊 Medication Center",
        "📄 Health Report",
        "🎯 Health Goals",
        "🇮🇳 Indian Healthcare"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("Stay Healthy ❤️")

st.sidebar.info(
"""
✔ AI Health Chatbot

✔ BMI Calculator

✔ Medication Tracker

✔ Health Reports

✔ Goal Tracking

✔ Indian Healthcare
"""
)

# ---------------- DASHBOARD ---------------- #

if menu == "🏠 Dashboard":

    st.header("📊 Personal Health Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("❤️ Heart Rate", "72 BPM")
    col2.metric("⚖ BMI", "22.4")
    col3.metric("💧 Water Intake", "2.5 L")
    col4.metric("🚶 Daily Steps", "6500")

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader("💊 Today's Medication")

        st.success("Vitamin D - 9:00 AM")

        st.info("Crocin - 8:00 PM")

        st.subheader("🎯 Goal Progress")

        st.progress(70)

        st.write("70% Goal Completed")

    with right:

        st.subheader("🌞 Today's Health Tip")

        st.success(
            "Drink at least 2.5L of water, walk for 30 minutes, "
            "and include fresh fruits in your meals."
        )

        st.subheader("😊 Overall Health Score")

        st.metric("Health Score", "92%", "+3%")

    st.markdown("---")

    st.subheader("📈 Weekly BMI Trend")

    bmi_data = [22.1, 22.0, 22.3, 22.5, 22.4, 22.2, 22.4]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(bmi_data, marker="o")

    ax.set_xlabel("Days")

    ax.set_ylabel("BMI")

    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("📅 Today's Summary")

    summary = pd.DataFrame(
        {
            "Category": [
                "Water",
                "Exercise",
                "Medicines",
                "Sleep"
            ],
            "Status": [
                "Completed",
                "Completed",
                "Pending",
                "7 Hours"
            ]
        }
    )

    st.table(summary)
# ---------------- AI CHATBOT ---------------- #

elif menu == "🤖 AI Chatbot":

    st.header("🤖 AI Health Assistant")

    st.write("Ask any general health-related question.")

    question = st.text_area(
        "Enter your health question",
        placeholder="Example: How can I reduce my blood pressure naturally?"
    )

    if st.button("🤖 Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Generating response..."):

                try:

                    answer = ask_health_question(question)

                    st.success("Response")

                    st.write(answer)

                except:

                    st.error("Unable to generate response.")


# ---------------- BMI CALCULATOR ---------------- #

elif menu == "📊 BMI Calculator":

    st.header("📊 BMI & Health Metrics")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=22
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            max_value=250.0
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=30.0,
            max_value=250.0
        )

        activity = st.selectbox(
            "Activity Level",
            [
                "Sedentary",
                "Lightly Active",
                "Moderately Active",
                "Very Active"
            ]
        )

    st.markdown("---")

    if st.button("Calculate BMI"):

        bmi = calculate_bmi(weight, height)

        st.success(f"Your BMI is {bmi}")

        if bmi < 18.5:

            status = "🔵 Underweight"

            recommendation = """
Increase healthy calories.

Eat protein-rich foods.

Strength training is recommended.
"""

        elif bmi < 25:

            status = "🟢 Healthy"

            recommendation = """
Maintain balanced diet.

Exercise 30 minutes daily.

Drink enough water.
"""

        elif bmi < 30:

            status = "🟠 Overweight"

            recommendation = """
Reduce sugary foods.

Walk at least 45 minutes daily.

Increase vegetables.
"""

        else:

            status = "🔴 Obese"

            recommendation = """
Consult a healthcare professional.

Follow a structured exercise plan.

Reduce processed food intake.
"""

        st.metric("BMI", bmi)

        st.info(status)

        st.subheader("Health Recommendation")

        st.write(recommendation)

        st.markdown("---")

        st.subheader("BMI Categories")

        bmi_chart = {
            "Underweight":18.5,
            "Healthy":24.9,
            "Overweight":29.9,
            "Obese":35
        }

        fig, ax = plt.subplots(figsize=(7,4))

        ax.bar(
            bmi_chart.keys(),
            bmi_chart.values()
        )

        ax.set_ylabel("BMI")

        ax.set_title("BMI Categories")

        st.pyplot(fig)

        st.markdown("---")

        st.subheader("Ideal Lifestyle Tips")

        tips = [

            "💧 Drink 2–3 litres of water",

            "🥗 Eat fresh fruits and vegetables",

            "🏃 Exercise at least 30 minutes",

            "😴 Sleep 7–8 hours",

            "🧘 Practice stress management"

        ]

        for tip in tips:

            st.write("✅", tip)
# ---------------- MEDICATION CENTER ---------------- #

elif menu == "💊 Medication Center":

    st.header("💊 Medication Center")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "➕ Add Medicine",
            "📋 My Medicines",
            "⚠ Interaction Checker",
            "🤖 AI Medicine Info"
        ]
    )

    # ---------------- ADD MEDICINE ---------------- #

    with tab1:

        st.subheader("Add New Medication")

        med_name = st.text_input("Medicine Name")

        med_time = st.time_input("Medicine Time")

        dosage = st.text_input("Dosage (Example: 500mg)")

        if st.button("➕ Add Medication"):

            add_new_medication(
                med_name,
                str(med_time)
            )

            st.success("Medication Added Successfully!")

    # ---------------- MEDICINE LIST ---------------- #

    with tab2:

        st.subheader("Your Medication List")

        medicines = list_medications()

        if medicines:

            st.table(medicines)

        else:

            st.info("No medications added yet.")

    # ---------------- INTERACTION CHECKER ---------------- #

    with tab3:

        st.subheader("Drug Interaction Checker")

        medicine1 = st.text_input("Medicine 1")

        medicine2 = st.text_input("Medicine 2")

        if st.button("Check Interaction"):

            result = check_interaction(
                medicine1,
                medicine2
            )

            st.warning(result)

    # ---------------- AI MEDICINE INFORMATION ---------------- #

    with tab4:

        st.subheader("🤖 AI Medicine Information")

        medicine = st.text_input(
            "Enter Medicine Name"
        )

        if st.button("Get AI Information"):

            if medicine == "":

                st.warning("Please enter medicine name.")

            else:

                try:

                    answer = ask_health_question(
                        f"""
Provide complete healthcare information about {medicine}.

Include:

1. Uses

2. Dosage

3. Side Effects

4. Precautions

5. Food Interactions

6. Important Warnings

Keep the response simple and easy to understand.
"""
                    )

                    st.success("Medicine Information")

                    st.write(answer)

                except:

                    st.error(
                        "Unable to fetch medicine information."
                    )
# ---------------- HEALTH REPORT ---------------- #

elif menu == "📄 Health Report":

    st.header("📄 Personal Health Report")

    today = datetime.now().strftime("%d %B %Y")

    st.info(f"Report Generated on: {today}")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("BMI", "22.4")

        st.metric("Health Score", "92%")

    with col2:

        medicines = list_medications()

        st.subheader("💊 Current Medications")

        if medicines:

            st.table(medicines)

        else:

            st.info("No medications available.")

    st.markdown("---")

    st.subheader("🤖 AI Generated Health Tips")

    if st.button("Generate Today's Tips"):

        try:

            tips = ask_health_question(f"""

Today's Date: {today}

Generate 5 different daily health tips.

Requirements:

- Keep every tip short.

- Make tips different every day.

- Include diet, exercise, sleep, hydration and mental health.

Do not repeat tips.

""")

            st.success("Today's Personalized Tips")

            st.write(tips)

        except:

            st.error("Unable to generate today's health tips.")

    st.markdown("---")

    st.subheader("📊 Overall Health Status")

    progress = 92

    st.progress(progress)

    st.success(f"Overall Health Score : {progress}%")



# ---------------- HEALTH GOALS ---------------- #

elif menu == "🎯 Health Goals":

    st.header("🎯 Health Goal Tracker")

    goal = st.selectbox(

        "Select Goal",

        [

            "Weight Loss",

            "Weight Gain",

            "Maintain Weight",

            "Improve Fitness",

            "Healthy Lifestyle"

        ]

    )

    target = st.number_input(

        "Target Weight (kg)",

        min_value=20,

        max_value=150,

        value=65

    )

    current = st.number_input(

        "Current Weight (kg)",

        min_value=20,

        max_value=150,

        value=70

    )

    progress = int((target/current)*100)

    progress = min(progress,100)

    st.progress(progress)

    st.write(f"Goal Progress : {progress}%")

    if st.button("Generate Goal Plan"):

        try:

            plan = ask_health_question(f"""

Generate a healthcare goal plan.

Goal: {goal}

Current Weight: {current}

Target Weight: {target}

Include:

Diet

Exercise

Water Intake

Sleep

Motivation

""")

            st.success("Personal Goal Plan")

            st.write(plan)

        except:

            st.error("Unable to generate plan.")
# ---------------- INDIAN HEALTHCARE ---------------- #

elif menu == "🇮🇳 Indian Healthcare":

    st.header("🇮🇳 Indian Healthcare Services")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🥗 Diet Planner",
            "🌿 Ayurvedic Assistant",
            "🩺 Doctor Finder",
            "🛡 Insurance Advisor"
        ]
    )

    # ---------------- DIET PLANNER ---------------- #

    with tab1:

        st.subheader("🥗 AI Indian Diet Planner")

        age = st.number_input("Age", 1, 100, 25)

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        weight = st.number_input(
            "Weight (kg)",
            20,
            200,
            70
        )

        height = st.number_input(
            "Height (cm)",
            50,
            250,
            170
        )

        goal = st.selectbox(
            "Health Goal",
            [
                "Weight Loss",
                "Weight Gain",
                "Maintain Weight"
            ]
        )

        diet = st.selectbox(
            "Food Preference",
            [
                "Vegetarian",
                "Non-Vegetarian"
            ]
        )

        if st.button("Generate Diet Plan"):

            with st.spinner("Preparing your personalized diet..."):

                response = ask_health_question(f"""

Create a personalized Indian diet plan.

Age: {age}

Gender: {gender}

Weight: {weight}

Height: {height}

Goal: {goal}

Food Preference: {diet}

Include:

Breakfast

Lunch

Snacks

Dinner

Water Intake

Foods to Avoid

Daily Calories

""")

                st.success("Your Personalized Diet Plan")

                st.write(response)

    # ---------------- AYURVEDIC ---------------- #

    with tab2:

        st.subheader("🌿 AI Ayurvedic Assistant")

        symptoms = st.text_area(
            "Describe your symptoms"
        )

        if st.button("Get Ayurvedic Advice"):

            with st.spinner("Generating Ayurvedic suggestions..."):

                answer = ask_health_question(f"""

Provide Ayurvedic suggestions.

Symptoms:

{symptoms}

Include:

Natural Remedies

Foods

Lifestyle Tips

Yoga

When to Consult a Doctor

""")

                st.success("Ayurvedic Guidance")

                st.write(answer)

 # ---------------- DOCTOR FINDER ---------------- #


    st.subheader("🩺 Find Doctors Near You")

    city = st.selectbox(
        "Select City",
        [
            "Hyderabad",
            "Delhi",
            "Bangalore",
            "Mumbai",
            "Chennai"
        ]
    )

    speciality = st.selectbox(
        "Select Specialization",
        [
            "General Physician",
            "Cardiologist",
            "Dermatologist",
            "Orthopedic",
            "Pediatrician",
            "Neurologist"
        ]
    )

    doctors = [

        {
            "city":"Hyderabad",
            "speciality":"Cardiologist",
            "name":"Dr. Ramesh Reddy",
            "hospital":"Apollo Hospitals",
            "experience":"15 Years",
            "rating":"⭐ 4.8",
            "phone":"+91-9876543210"
        },

        {
            "city":"Hyderabad",
            "speciality":"General Physician",
            "name":"Dr. Priya Sharma",
            "hospital":"Yashoda Hospitals",
            "experience":"10 Years",
            "rating":"⭐ 4.7",
            "phone":"+91-9123456789"
        },

        {
            "city":"Delhi",
            "speciality":"Dermatologist",
            "name":"Dr. Amit Singh",
            "hospital":"Fortis Hospital",
            "experience":"12 Years",
            "rating":"⭐ 4.9",
            "phone":"+91-9988776655"
        },

        {
            "city":"Bangalore",
            "speciality":"Orthopedic",
            "name":"Dr. Rahul Kumar",
            "hospital":"Manipal Hospital",
            "experience":"14 Years",
            "rating":"⭐ 4.8",
            "phone":"+91-9345678912"
        },

        {
            "city":"Mumbai",
            "speciality":"Neurologist",
            "name":"Dr. Neha Mehta",
            "hospital":"Kokilaben Hospital",
            "experience":"18 Years",
            "rating":"⭐ 4.9",
            "phone":"+91-9870012345"
        },

        {
            "city":"Chennai",
            "speciality":"Pediatrician",
            "name":"Dr. Lakshmi Iyer",
            "hospital":"Apollo Chennai",
            "experience":"11 Years",
            "rating":"⭐ 4.8",
            "phone":"+91-9444455555"
        }

    ]

    if st.button("🔍 Search Doctors"):

        found = False

        for doctor in doctors:

            if doctor["city"] == city and doctor["speciality"] == speciality:

                found = True

                with st.container():

                    st.markdown("---")

                    st.subheader(f"👨‍⚕️ {doctor['name']}")

                    col1,col2 = st.columns(2)

                    with col1:

                        st.write("🏥 Hospital:",doctor["hospital"])
                        st.write("🩺 Specialization:",doctor["speciality"])
                        st.write("⭐ Rating:",doctor["rating"])

                    with col2:

                        st.write("📅 Experience:",doctor["experience"])
                        st.write("📞 Contact:",doctor["phone"])
                        st.success("Available for Appointment")

        if not found:

            st.error("No doctors found.")
    # ---------------- INSURANCE ---------------- #

    with tab4:

        st.subheader("🛡 AI Health Insurance Advisor")

        age = st.number_input(
            "Your Age",
            18,
            100,
            30
        )

        family = st.number_input(
            "Family Members",
            1,
            10,
            2
        )

        budget = st.selectbox(

            "Monthly Budget",

            [

                "₹500",

                "₹1000",

                "₹2000",

                "₹5000"

            ]

        )

        if st.button("Suggest Insurance"):

            with st.spinner("Finding suitable insurance..."):

                advice = ask_health_question(f"""

Suggest a health insurance plan.

Age:

{age}

Family Members:

{family}

Budget:

{budget}

Include:

Coverage

Benefits

Who should choose it

Precautions

""")

                st.success("Insurance Recommendation")

                st.write(advice)
