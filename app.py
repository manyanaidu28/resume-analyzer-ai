import streamlit as st
import json
import os
import pandas as pd
import google.generativeai as genai
from fpdf import FPDF
import PyPDF2
from datetime import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Resume Analyzer AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- GEMINI API ----------------

GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- PROFESSIONAL UI ----------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: sans-serif;
}

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
    color: white;
}

/* Inputs */
.stTextInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid #334155 !important;
}

.stTextArea textarea {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid #334155 !important;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 16px;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    padding: 16px;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: #1e293b;
    border-radius: 16px;
    padding: 15px;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE ----------------

if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)

with open("users.json", "r") as f:
    users = json.load(f)

# ---------------- SESSION ----------------

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "signup"

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIGNUP PAGE ----------------

if st.session_state.page == "signup":

    st.markdown("""
    <h1 style='text-align:center;'>
    📝 Create Account
    </h1>
    """, unsafe_allow_html=True)

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("🚀 Create Account"):

        if email in users:

            st.error("User already exists ❌")

        elif email == "" or password == "":

            st.warning("Fill all fields ⚠️")

        else:

            users[email] = password

            with open("users.json", "w") as f:
                json.dump(users, f)

            st.success(
                "Account created successfully ✅"
            )

    if st.button("🔑 Already have account? Login"):

        st.session_state.page = "login"

        st.rerun()

# ---------------- LOGIN PAGE ----------------

elif st.session_state.page == "login":

    st.markdown("""
    <h1 style='text-align:center;'>
    🔐 Login
    </h1>
    """, unsafe_allow_html=True)

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("🚀 Login"):

        if email in users and users[email] == password:

            st.session_state.user = email

            st.session_state.page = "dashboard"

            st.rerun()

        else:

            st.error("Invalid credentials ❌")

    if st.button("📝 Create New Account"):

        st.session_state.page = "signup"

        st.rerun()

# ---------------- DASHBOARD ----------------

elif st.session_state.page == "dashboard":

    st.title("🚀 Resume Analyzer AI")

    st.markdown("""
    ### Analyze your resume using AI & improve your career 🔥
    """)

    menu = st.selectbox(
        "📱 Navigation",
        [
            "🏠 Dashboard",
            "📄 Resume Analyzer",
            "📊 Analytics",
            "💼 Job Recommendations",
            "👤 Profile"
        ]
    )

    if st.button("🚪 Logout"):

        st.session_state.user = None

        st.session_state.page = "login"

        st.rerun()

    # ---------------- HOME ----------------

    if menu == "🏠 Dashboard":

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Resume Checks", "120+")

        with col2:
            st.metric("🤖 AI Accuracy", "95%")

        with col3:
            st.metric("🚀 ATS Success", "90%")

        st.success(
            f"Welcome {st.session_state.user} 🚀"
        )

    # ---------------- RESUME ANALYZER ----------------

    elif menu == "📄 Resume Analyzer":

        st.subheader("📄 Upload Resume")

        skills = [
            "python",
            "sql",
            "machine learning",
            "excel",
            "communication",
            "data analysis",
            "deep learning",
            "nlp",
            "power bi",
            "tableau",
            "react",
            "java",
            "c++",
            "aws",
            "cloud",
            "javascript"
        ]

        uploaded_file = st.file_uploader(
            "📄 Upload Resume",
            type=["pdf", "txt"]
        )

        resume = ""

        if uploaded_file is not None:

            if uploaded_file.type == "application/pdf":

                pdf_reader = PyPDF2.PdfReader(
                    uploaded_file
                )

                for page in pdf_reader.pages:

                    text = page.extract_text()

                    if text:
                        resume += text

            else:

                resume = uploaded_file.read().decode(
                    "utf-8"
                )

        resume_input = st.text_area(
            "📋 Or paste your resume here"
        )

        if resume_input:
            resume = resume_input

        if st.button("🔍 Analyze Resume"):

            if resume.strip() == "":

                st.warning(
                    "Please upload or paste resume ⚠️"
                )

            else:

                resume = resume.lower()

                found_skills = [
                    s for s in skills if s in resume
                ]

                missing_skills = [
                    s for s in skills if s not in resume
                ]

                score = int(
                    (len(found_skills) / len(skills)) * 100
                )

                st.subheader("📊 ATS Results")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "🚀 ATS Score",
                        f"{score}%"
                    )

                with col2:
                    st.metric(
                        "✅ Skills Found",
                        len(found_skills)
                    )

                st.progress(score)

                st.success(
                    f"✅ Found Skills: {', '.join(found_skills)}"
                )

                st.error(
                    f"❌ Missing Skills: {', '.join(missing_skills[:5])}"
                )

                feedback = f"""
🔥 Resume Feedback

✅ Skills Found:
{', '.join(found_skills)}

❌ Missing Skills:
{', '.join(missing_skills[:5])}

🚀 Add:
- Projects
- Certifications
- Internships
- Achievements
"""

                st.info(feedback)

                # ---------------- GEMINI AI ----------------

                with st.spinner(
                    "🤖 Gemini AI analyzing..."
                ):

                    response = model.generate_content(
                        f"""
Analyze this resume professionally.

Resume:
{resume}

Give:
1. ATS improvement tips
2. Missing skills
3. Career suggestions
4. Resume strengths
5. Weaknesses
6. Interview preparation tips
"""
                    )

                st.subheader("🤖 AI Analysis")

                st.write(response.text)

                # ---------------- SAVE HISTORY ----------------

                st.session_state.history.append({

                    "date": str(datetime.now())[:19],
                    "score": score,
                    "skills": found_skills

                })

                # ---------------- PDF REPORT ----------------

                pdf = FPDF()

                pdf.add_page()

                pdf.set_font(
                    "Arial",
                    size=12
                )

                pdf.multi_cell(
                    0,
                    10,
                    txt=f"""
ATS Score: {score}%

Found Skills:
{', '.join(found_skills)}

Missing Skills:
{', '.join(missing_skills[:5])}

AI Feedback:
{response.text}
"""
                )

                pdf.output("report.pdf")

                with open(
                    "report.pdf",
                    "rb"
                ) as file:

                    st.download_button(
                        "📥 Download PDF Report",
                        file,
                        file_name="resume_report.pdf"
                    )

    # ---------------- ANALYTICS ----------------

    elif menu == "📊 Analytics":

        st.subheader("📈 Analytics")

        if len(st.session_state.history) == 0:

            st.warning("No history available")

        else:

            df = pd.DataFrame(
                st.session_state.history
            )

            st.dataframe(df)

            st.line_chart(df["score"])

    # ---------------- JOB RECOMMENDATIONS ----------------

    elif menu == "💼 Job Recommendations":

        st.subheader("💼 AI Job Recommendations")

        st.info("""
🔥 Recommended Roles:

• Python Developer  
• Data Analyst  
• Machine Learning Engineer  
• Frontend Developer  
• AI Engineer  
• Cloud Engineer  
""")

    # ---------------- PROFILE ----------------

    elif menu == "👤 Profile":

        st.subheader("👤 Profile")

        st.success(
            f"Logged in as: {st.session_state.user}"
        )

        st.info("""
🚀 Premium Features Coming Soon:

• AI Mock Interviews  
• Resume Templates  
• Cover Letter Generator  
• LinkedIn Optimizer  
• Admin Dashboard  
""")
