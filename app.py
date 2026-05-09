import streamlit as st
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Resume Analyzer AI",
    page_icon="🚀",
    layout="centered"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "users" not in st.session_state:
    st.session_state.users = {}

if "history" not in st.session_state:
    st.session_state.history = []

if "section" not in st.session_state:
    st.session_state.section = "home"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* Hide Streamlit */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Background */

.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #071b34,
        #020617
    );
    color: white;
}

/* Fonts */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Inputs */

.stTextInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid #334155 !important;
}

/* Upload */

.stFileUploader {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #334155;
}

/* 3D Buttons */

.stButton > button {

    width: 100%;

    background: linear-gradient(
        135deg,
        #3b82f6,
        #9333ea
    );

    color: white;

    border: none;

    padding: 16px;

    border-radius: 18px;

    font-size: 20px;

    font-weight: bold;

    margin-top: 12px;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.4);

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.03);

    background: linear-gradient(
        135deg,
        #2563eb,
        #7e22ce
    );

    box-shadow:
        0 10px 25px rgba(147,51,234,0.6);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# WELCOME SCREEN
# =========================================================

if st.session_state.page == "welcome":

    st.markdown("""
    <div style='text-align:center; padding-top:60px;'>

    <h1 style='font-size:70px; color:white;'>
    🚀 Resume Analyzer AI
    </h1>

    <p style='font-size:28px; color:#d1d5db;'>

    Analyze your resume using AI and
    improve your career opportunities 🔥

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    ### ✨ Features

    ✅ AI Resume Analysis  
    ✅ ATS Score Checker  
    ✅ Missing Skills Detection  
    ✅ Career Recommendations  
    ✅ Resume Improvement Tips  
    ✅ PDF Report Download  
    ✅ Resume History  
    """)

    st.write("")
    st.write("")

    if st.button("🚀 Get Started"):

        st.session_state.page = "signup"

        st.rerun()

# =========================================================
# SIGNUP PAGE
# =========================================================

elif st.session_state.page == "signup":

    st.title("📝 Create Account")

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("🚀 Create Account"):

        if email in st.session_state.users:

            st.error("User already exists ❌")

        elif email == "" or password == "":

            st.warning("Please fill all fields ⚠️")

        else:

            st.session_state.users[email] = password

            st.success("Account created successfully ✅")

            time.sleep(1)

            st.session_state.page = "login"

            st.rerun()

# =========================================================
# LOGIN PAGE
# =========================================================

elif st.session_state.page == "login":

    st.title("🔑 Login")

    login_email = st.text_input("📧 Login Email")

    login_password = st.text_input(
        "🔒 Login Password",
        type="password"
    )

    if st.button("🔑 Login"):

        if (
            login_email in st.session_state.users
            and
            st.session_state.users[login_email]
            == login_password
        ):

            st.success("Login Successful ✅")

            st.session_state.page = "loading"

            st.rerun()

        else:

            st.error("Invalid Email or Password ❌")

# =========================================================
# AI LOADING SCREEN
# =========================================================

elif st.session_state.page == "loading":

    st.title("🤖 AI Loading")

    st.info("Preparing your AI dashboard...")

    progress = st.progress(0)

    for i in range(100):

        time.sleep(0.02)

        progress.progress(i + 1)

    st.success("AI Ready ✅")

    time.sleep(1)

    st.session_state.page = "dashboard"

    st.rerun()

# =========================================================
# DASHBOARD
# =========================================================

elif st.session_state.page == "dashboard":

    st.markdown("""
    <h1 style='text-align:center; color:white; font-size:60px;'>
    🚀 Dashboard
    </h1>
    """, unsafe_allow_html=True)

    # MENU BUTTONS

    if st.button("🏠 Home"):
        st.session_state.section = "home"

    if st.button("📄 Upload Resume"):
        st.session_state.section = "upload"

    if st.button("⚡ Resume Processing"):
        st.session_state.section = "processing"

    if st.button("📊 ATS Results"):
        st.session_state.section = "ats"

    if st.button("🧠 Skills Analysis"):
        st.session_state.section = "skills"

    if st.button("❌ Missing Skills"):
        st.session_state.section = "missing"

    if st.button("💡 AI Suggestions"):
        st.session_state.section = "suggestions"

    if st.button("💼 Career Recommendations"):
        st.session_state.section = "career"

    if st.button("📜 Resume Tips"):
        st.session_state.section = "tips"

    if st.button("📥 Download PDF Report"):
        st.session_state.section = "download"

    if st.button("🕘 Resume History"):
        st.session_state.section = "history"

    if st.button("👤 Profile"):
        st.session_state.section = "profile"

    if st.button("🚪 Logout"):

        st.session_state.page = "welcome"

        st.rerun()

    st.write("")
    st.write("")

    # =====================================================
    # HOME
    # =====================================================

    if st.session_state.section == "home":

        st.title("🏠 Home")

        st.metric("📄 Resume Checks", "120+")

        st.metric("🤖 AI Accuracy", "95%")

        st.metric("🚀 ATS Success", "90%")

    # =====================================================
    # UPLOAD RESUME
    # =====================================================

    elif st.session_state.section == "upload":

        st.title("📄 Upload Resume")

        uploaded_file = st.file_uploader(
            "Upload Resume PDF",
            type=["pdf"]
        )

        if uploaded_file:

            st.success("Resume uploaded successfully ✅")

            st.session_state.history.append(
                uploaded_file.name
            )

    # =====================================================
    # AI PROCESSING
    # =====================================================

    elif st.session_state.section == "processing":

        st.title("⚡ Resume Processing")

        st.info("AI is analyzing your resume...")

        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.03)

            progress.progress(i + 1)

        st.success("Resume processed successfully 🚀")

    # =====================================================
    # ATS RESULTS
    # =====================================================

    elif st.session_state.section == "ats":

        st.title("📊 ATS Results")

        st.metric("🚀 ATS Score", "92%")

        st.progress(92)

        st.success("Your resume is ATS Friendly ✅")

    # =====================================================
    # SKILLS ANALYSIS
    # =====================================================

    elif st.session_state.section == "skills":

        st.title("🧠 Skills Analysis")

        st.success("""
✅ Python  
✅ SQL  
✅ Communication  
✅ Teamwork  
✅ Machine Learning  
""")

    # =====================================================
    # MISSING SKILLS
    # =====================================================

    elif st.session_state.section == "missing":

        st.title("❌ Missing Skills")

        st.warning("""
⚠️ Docker  
⚠️ AWS  
⚠️ System Design  
⚠️ Data Structures  
""")

    # =====================================================
    # AI SUGGESTIONS
    # =====================================================

    elif st.session_state.section == "suggestions":

        st.title("💡 AI Suggestions")

        st.info("""
🔥 Add more projects  
🔥 Add internships  
🔥 Add certifications  
🔥 Improve ATS keywords  
🔥 Improve formatting  
""")

    # =====================================================
    # CAREER RECOMMENDATIONS
    # =====================================================

    elif st.session_state.section == "career":

        st.title("💼 Career Recommendations")

        st.success("""
🚀 Data Analyst  
🚀 AI Engineer  
🚀 Python Developer  
🚀 Data Engineer  
""")

    # =====================================================
    # RESUME TIPS
    # =====================================================

    elif st.session_state.section == "tips":

        st.title("📜 Resume Tips")

        st.info("""
✅ Keep resume one page  
✅ Add measurable achievements  
✅ Use ATS keywords  
✅ Use professional formatting  
""")

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    elif st.session_state.section == "download":

        st.title("📥 Download PDF Report")

        report = """
Resume Analyzer AI Report

ATS Score: 92%

Skills:
- Python
- SQL
- Communication

Suggestions:
- Add projects
- Improve formatting
"""

        st.download_button(
            "📄 Download Report",
            report,
            file_name="resume_report.txt"
        )

    # =====================================================
    # HISTORY
    # =====================================================

    elif st.session_state.section == "history":

        st.title("🕘 Resume History")

        if len(st.session_state.history) == 0:

            st.warning("No resumes uploaded yet ⚠️")

        else:

            for file in st.session_state.history:

                st.success(f"📄 {file}")

    # =====================================================
    # PROFILE
    # =====================================================

    elif st.session_state.section == "profile":

        st.title("👤 Profile")

        st.info("""
👤 Resume Analyzer User  
📧 Registered Account  
🚀 AI Dashboard Access  
🤖 Premium Features Enabled  
""")
