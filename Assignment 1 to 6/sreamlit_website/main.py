import streamlit as st
from streamlit_option_menu import option_menu

# App Config
st.set_page_config(page_title="My First Website", layout="wide")

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "About", "Contact"],
        icons=["house", "person", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# ---------------------- HOME PAGE ----------------------
if selected == "Home":
    st.title("🏠 Welcome to My Website")
    st.write("This is the home page of your first Streamlit website.")
    name = st.text_input("Enter your name")
    if name:
        st.success(f"Hello, {name}! Welcome aboard. 👋")

# ---------------------- ABOUT PAGE ----------------------
elif selected == "About":
    st.title("👩‍💻 About Me")
    st.write("""
        Hi! I'm Kinza, a passionate learner exploring the world of web development and AI.
        
        - 💻 I know HTML, CSS, JavaScript, TypeScript, Next.js.
        - 📚 Also  a medical student at Jinnah Medical  University
        - 🎯 This is my first Streamlit project!
    """)

# ---------------------- CONTACT PAGE ----------------------
elif selected == "Contact":
    st.title("📞 Contact Me")
    st.write("You can reach me through the form below:")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully! 🚀")
        else:
            st.error("Please fill all the fields.")
