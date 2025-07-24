import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="EduTrack Dashboard", layout="wide")

# Custom CSS for background and styling
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtjp9Lv1Iy-12rXcmiQ8xZUlNM6DVKm1GPsA&s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    body {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Dashboard Title with Logo
st.markdown("""
    <div style='display: flex; align-items: center;'>
        <img src='https://t4.ftcdn.net/jpg/05/91/40/47/360_F_591404733_XI6dw0OZMfxCsZLqzmY8BcWbzf2QwZdK.jpg' width='60' style='margin-right: 15px;'>
        <h1 style='margin: 0;'>Student Performance Dashboard</h1>
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📂 Navigation")
selected_section = st.sidebar.radio("Go to:", [
    "View Data",
    "Marks Comparison",
    "Attendance Comparison",
    "Leaderboard",
    "Detain List"
])

# File Upload
uploaded_file = st.sidebar.file_uploader("📥 Upload Student CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Check required columns
    required_cols = {"ID", "Name", "Class", "Marks", "Attendance"}
    if not required_cols.issubset(df.columns):
        st.error("❌ CSV must include: ID, Name, Class, Marks, Attendance")
    else:
        # Section: View Data
        if selected_section == "View Data":
            st.subheader("📄 Student Data")
            st.dataframe(df)

        # Section: Marks Comparison
        elif selected_section == "Marks Comparison":
            st.subheader("📊 Marks Comparison")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(df["Name"], df["Marks"], color="skyblue")
            ax.set_xlabel("Student")
            ax.set_ylabel("Marks")
            ax.set_title("Marks of Students")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # Section: Attendance Comparison
        elif selected_section == "Attendance Comparison":
            st.subheader("📊 Attendance Comparison")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            ax2.bar(df["Name"], df["Attendance"], color="orange")
            ax2.set_xlabel("Student")
            ax2.set_ylabel("Attendance (%)")
            ax2.set_title("Attendance of Students")
            plt.xticks(rotation=45)
            st.pyplot(fig2)

        # Section: Leaderboard
        elif selected_section == "Leaderboard":
            st.subheader("🏆 Top 5 Students by Marks")
            leaderboard = df.sort_values(by="Marks", ascending=False).head(5)
            st.dataframe(leaderboard[["Name", "Class", "Marks"]])

        # Section: Detain List
        elif selected_section == "Detain List":
            st.subheader("🚫 Detain List (Attendance < 5%)")
            detain_list = df[df["Attendance"] < 5]
            if not detain_list.empty:
                st.dataframe(detain_list[["Name", "Class", "Attendance"]])
            else:
                st.success("🎉 No students to detain!")

else:
    st.info("📂 Please upload a student CSV file from the sidebar to continue.")
