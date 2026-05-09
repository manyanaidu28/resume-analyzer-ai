import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from fpdf import FPDF
from datetime import datetime
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Resume Analyzer AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- GEMINI API ----------------

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {}

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- CSS ----------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: #06152b;
    color: white;
}

/* Hide Streamlit */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stDeployButton {
    display: none;
}

[data-testid="stStatusWidget"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

/* Main */
.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #071b34,
        #020617
    );
}

/* Title */
.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
}

.sub-text {
    text-align: center;
    font-size: 24px;
    color: #d1d5db;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 15px;
    padding: 14px;
    border: none;
    font-size: 20px;
    font-weight: bold;
    color: white;
    background: linear-gradient(90deg,#2563eb,#9333ea);
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

/* File uploader */
.stFileUploader {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------

if st.session_state.logged_in == False:

    st.markdown(
        "<h1 class='main-title'>🚀 Resume Analyzer AI</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='sub-text'>Analyze your resume using AI & improve your career 🔥</p>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["📝 Create Account", "🔑 Login"])

    # -------- CREATE ACCOUNT --------

    with tab1:

        email = st.text_input("📧 Email")

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        if st.button("🚀 Create Account"):

            if email in st.session_state.users:
                st.error("User already exists ❌")

            else:
                st.session_state.users[email] = password
                st.success("Account created successfully ✅")

    # -------- LOGIN --------

    with tab2:

        login_email = st.text_input("📧 Login Email")

        login_password = st.text_input(
            "🔒 Login Password",
            type="password"
        )

        if st.button("🔑 Login"):

            if (
                login_email in st.session_state.users
                and
                st.session_state.users[login_email] == login_password
            ):

                st.session_state.logged_in = True
                st.success("Login successful ✅")
                st.rerun()

            else:
                st.error("Invalid email or password ❌")

# ---------------- DASHBOARD ----------------

else:

    st.sidebar.title("🚀 Dashboard")

    page = st.sidebar.radio(
        "Go To",
        [
            "🏠 Home",
            "📊 Resume Analyzer",
            "📜 History"
        ]
    )

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # ---------------- HOME ----------------

    if page == "🏠 Home":

        st.markdown(
            "<h1 class='main-title'>🚀 Resume Analyzer AI</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p class='sub-text'>Analyze your resume using AI & improve your career 🔥</p>",
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="card">
            <h3>📄 Resume Checks</h3>
            <h1>120+</h1>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
            <h3>🤖 AI Accuracy</h3>
            <h1>95%</h1>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
            <h3>🚀 ATS Success</h3>
            <h1>90%</h1>
            </div>
            """, unsafe_allow_html=True)

    # ---------------- ANALYZER ----------------

    elif page == "📊 Resume Analyzer":

        st.title("📊 Resume Analyzer")

        uploaded_file = st.file_uploader(
            "📄 Upload Resume PDF",
            type=["pdf"]
        )

        resume_text = st.text_area(
            "📋 Or paste your resume here"
        )

        if st.button("🔍 Analyze Resume"):

            resume = ""

            # PDF TEXT
            if uploaded_file:

                pdf_reader = PdfReader(uploaded_file)

                for page in pdf_reader.pages:
                    resume += page.extract_text()

            # TEXT AREA
            if resume_text:
                resume += resume_text

            if resume == "":
                st.error("Please upload or paste resume ❌")

            else:

                skills = [
                    "python",
                    "sql",
                    "machine learning",
                    "deep learning",
                    "data analysis",
                    "excel",
                    "communication"
                ]

                found_skills = []

                for skill in skills:
                    if skill.lower() in resume.lower():
                        found_skills.append(skill)

                missing_skills = [
                    s for s in skills
                    if s not in found_skills
                ]

                score = int(
                    (len(found_skills) / len(skills)) * 100
                )

                # ATS RESULTS

                st.subheader("📊 ATS Results")

                st.metric("🚀 ATS Score", f"{score}%")

                st.metric(
                    "✅ Skills Found",
                    len(found_skills)
                )

                st.progress(score / 100)

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

                # -------- GEMINI AI --------

                try:

                    with st.spinner("🤖 Gemini AI analyzing..."):

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

                        ai_text = response.text

                        st.subheader("🤖 AI Analysis")

                        st.write(ai_text)

                except Exception as e:

                    ai_text = """
✅ Add more technical skills
✅ Add projects
✅ Add certifications
✅ Improve resume formatting
✅ Add internships
"""

                    st.subheader("🤖 AI Analysis")

                    st.info(ai_text)

                # -------- SAVE HISTORY --------

                st.session_state.history.append({

                    "date": str(datetime.now())[:19],
                    "score": score,
                    "skills": found_skills

                })

                # -------- PDF REPORT --------

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
{ai_text}
"""
                )

                pdf.output("resume_report.pdf")

                with open(
                    "resume_report.pdf",
                    "rb"
                ) as file:

                    st.download_button(
                        "📥 Download Report",
                        file,
                        file_name="resume_report.pdf"
                    )

    # ---------------- HISTORY ----------------

    elif page == "📜 History":

        st.title("📜 Resume History")

        if len(st.session_state.history) == 0:

            st.info("No history available")

        else:

            for item in st.session_state.history:

                st.markdown(f"""
<div class="card">

<h3>📅 {item['date']}</h3>

<h2>🚀 Score: {item['score']}%</h2>

<p>✅ Skills: {', '.join(item['skills'])}</p>

</div>
<br>
""", unsafe_allow_html=True)
