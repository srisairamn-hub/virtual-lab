import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Thermo Lab 360",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f4ff;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🧪 THERMO LAB 360")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Navigation", 
    ["Student Details", "Dashboard", "Gas Expansion Simulator", "Gibbs Free Energy Calculator"]
)

# Persistent State Management
if 'student' not in st.session_state:
    st.session_state.student = {
        "name": "N.Sri Sairam",
        "reg_no": "RA2611003050059",
        "dept": "CSE",
        "course": "Thermodynamics – Module III"
    }

# --- SECTION 1: STUDENT DETAILS ---
if menu == "Student Details":
    st.title("👤 Student Details & Registration")
    st.markdown("Enter or update your academic credentials below.")
    
    with st.form("student_form"):
        name = st.text_input("Full Name", value=st.session_state.student["name"])
        reg_no = st.text_input("Register Number", value=st.session_state.student["reg_no"])
        dept = st.text_input("Department", value=st.session_state.student["dept"])
        course = st.text_input("Course / Class", value=st.session_state.student["course"])
        
        submitted = st.form_submit_button("Save Student Details")
        if submitted:
            st.session_state.student = {
                "name": name,
                "reg_no": reg_no,
                "dept": dept,
                "course": course
            }
            st.success("Student details saved successfully! Navigate to Dashboard to view your progress.")

# --- SECTION 2: DASHBOARD ---
elif menu == "Dashboard":
    st.title("📊 Student Dashboard")
    stud = st.session_state.student
    
    st.markdown(f"### Welcome back, **{stud['name']}**!")
    st.markdown(f"**Department:** {stud['dept']} | **Register No:** {stud['reg_no']}")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Completed Lessons", "24 / 32")
    col2.metric("Assignments Done", "8 / 10")
    col3.metric("Quiz Score", "92%")
    col4.metric("Overall Mastery", "78%")
    
    st.markdown("### Syllabus Progress")
    st.progress(0.78)

# --- SECTION 3: GAS EXPANSION SIMULATOR ---
elif menu == "Gas Expansion Simulator":
    st.title("🔬 Virtual Lab: Gas Expansion & Piston Simulator")
    st.markdown("Adjust volume and temperature to observe pressure response using the Ideal Gas Law ($PV = nRT$).")
    
    col_ctrl, col_viz = st.columns([1, 1])
    
    with col_ctrl:
        st.subheader("Control Panel")
        volume = st.slider("Volume ($V$ in Liters)", min_value=2.0, max_value=30.0, value=10.0, step=0.5)
        temperature = st.slider("Temperature ($T$ in Kelvin)", min_value=100.0, max_value=600.0, value=300.0, step=10.0)
        
        # Calculation: P = nRT / V (assuming n = 1 mol, R = 0.0821 L·atm/(mol·K))
        n = 1.0
        R = 0.0821
        pressure = (n * R * temperature) / volume
        
        st.info(f"**Calculated Pressure ($P$):** {pressure:.2f} atm")
        
        if volume > 18:
            st.warning("State: Expansion Phase")
        elif volume < 8:
            st.warning("State: Compression Phase")
        else:
            st.success("State: Equilibrium Phase")

    with col_viz:
        st.subheader("Pressure vs Volume Isotherm")
        # Generate Isotherm plot
        v_range = np.linspace(2, 30, 100)
        p_range = (n * R * temperature) / v_range
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(v_range, p_range, color='#2563eb', linewidth=2.5, label=f'T = {temperature}K')
        ax.scatter([volume], [pressure], color='red', s=100, zorder=5, label='Current State')
        ax.set_xlabel('Volume (L)')
        ax.set_ylabel('Pressure (atm)')
        ax.set_title('Isothermal Expansion Curve')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        st.pyplot(fig)

# --- SECTION 4: GIBBS FREE ENERGY CALCULATOR ---
elif menu == "Gibbs Free Energy Calculator":
    st.title("⚡ Gibbs Free Energy & Spontaneity Calculator")
    st.markdown("Calculate $\\Delta G = \\Delta H - T\\Delta S$ to determine reaction spontaneity.")
    
    delta_h = st.number_input("Enthalpy Change ($\\Delta H$ in kJ/mol)", value=-50.0)
    delta_s = st.number_input("Entropy Change ($\\Delta S$ in J/mol·K)", value=-100.0)
    temp = st.number_input("Temperature ($T$ in Kelvin)", value=298.0)
    
    # Calculation (converting J to kJ for entropy term)
    delta_g = delta_h - (temp * (delta_s / 1000.0))
    
    st.markdown("---")
    st.metric(label="Gibbs Free Energy Change ($\\Delta G$)", value=f"{delta_g:.2f} kJ/mol")
    
    if delta_g < 0:
        st.success("Result: The process is **Spontaneous** ($\\Delta G < 0$).")
    elif delta_g > 0:
        st.error("Result: The process is **Non-Spontaneous** ($\\Delta G > 0$).")
    else:
        st.warning("Result: The system is at **Equilibrium** ($\\Delta G = 0$).")
Step-by-Step GitHub & Deployment Guide
Create a GitHub Repository:

Go to GitHub Sign in to GitHub and create a new public repository named streamlit-thermo-app.

Upload Files:

Upload your app.py and requirements.txt files directly to the repository or push them via Git:

Bash
git init
git add .
git commit -m "Initial commit for Thermo Lab Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/streamlit-thermo-app.git
git push -u origin main
