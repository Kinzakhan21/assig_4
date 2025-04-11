import streamlit as st

# Page setup
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

# --- Background gradient using simple CSS ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f3e7e9, #e3eeff);
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>💪 Simple BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("### Just enter your height & weight and let me do the math 😉")

st.markdown("---")

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Your Weight (kg) ⚖️", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Your Height (cm) 📏", min_value=1.0, format="%.2f")

# --- BMI Calculation ---
if st.button("Let's calculate! 🚀"):
    # Convert cm to m
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Show result
    st.success(f"👉 Your BMI is **{bmi:.2f}**")

    # Status logic
    if bmi < 18.5:
        st.warning("You're **underweight**. Eat well & take care! 🥦")
        status = "Underweight"
        progress = 20
    elif 18.5 <= bmi < 24.9:
        st.info("Nice! You're in the **healthy range**. 🎉")
        status = "Normal"
        progress = 50
    elif 25 <= bmi < 29.9:
        st.warning("Hmm, you're **overweight**. Time to move a bit more 🏃‍♀️")
        status = "Overweight"
        progress = 75
    else:
        st.error("You're in the **obese** range. Please consult a doctor ❤️‍🩹")
        status = "Obese"
        progress = 100

    # Visual Progress
    st.markdown(f"### Your Status: {status}")
    st.progress(progress)

    # BMI Range Info
    st.markdown("##### BMI Chart 📊")
    st.markdown("""
    | Category       | BMI Range       |
    |----------------|------------------|
    | Underweight    | Less than 18.5   |
    | Normal         | 18.5 – 24.9      |
    | Overweight     | 25 – 29.9        |
    | Obese          | 30 or more       |
    """)

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with 🩷 by Kinza | Powered by Streamlit</p>", unsafe_allow_html=True)
