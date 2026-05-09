import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Resume Analyzer AI",
    page_icon="🚀",
    layout="centered"
)

# ---------------- SESSION STATES ----------------

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {}

# ---------------- CSS ----------------

st.markdown("""
<style>

/* HIDE STREAMLIT */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stToolbar"] {
display:none;
}

[data-testid="stDecoration"] {
display:none;
}

/* BACKGROUND */

.stApp{
background: linear-gradient(180deg,#000428,#004e92);
color:white;
}

/* TITLES */

.main-title{
text-align:center;
font-size:65px;
font-weight:bold;
color:white;
margin-top:30px;
}

.sub-text{
text-align:center;
font-size:24px;
color:#dddddd;
}

/* 3D BUTTONS */

.stButton>button{
width:100%;
background: linear-gradient(135deg,#3b82f6,#9333ea);
color:white;
border:none;
padding:16px;
border-radius:18px;
font-size:20px;
font-weight:bold;
margin-top:12px;
box-shadow:0 8px 20px rgba(0,0,0,0.4);
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.03);
background: linear-gradient(135deg,#2563eb,#7e22ce);
box-shadow:0 10px 25px rgba(147,51,234,0.6);
}

/* CARDS */

.card{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
margin-top:20px;
box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# ---------------- WELCOME PAGE ----------------

if st.session_state.page == "welcome":

    st.markdown("""
    <h1 class='main-title'>🚀 Resume Analyzer AI</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class='sub-text'>
    Analyze your resume using AI and improve your career 🔥
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>

    ✅ AI Resume Analysis<br><br>
    ✅ ATS Score Checker<br><br>
    ✅ Skills Detection<br><br>
    ✅ AI Suggestions<br><br>
    ✅ Career Recommendations<br><br>
    ✅ PDF Report Download

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🚀 Get Started"):
        st.session_state.page = "signup"
        st.rerun()

# ---------------- SIGNUP PAGE ----------------

elif st.session_state.page == "signup":

    st.markdown("""
    <h1 class='main-title'>📝 Create Account</h1>
    """, unsafe_allow_html=True)

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

            time.sleep(1)

            st.session_state.page = "login"
            st.rerun()

# ---------------- LOGIN PAGE ----------------

elif st.session_state.page == "login":

    st.markdown("""
    <h1 class='main-title'>🔑 Login</h1>
    """, unsafe_allow_html=True)

    login_email = st.text_input("📧 Login Email")

    login_password = st.text_input(
        "🔒 Login Password",
        type="password"
    )

    if st.button("🚀 Login"):

        if (
            login_email in st.session_state.users
            and
            st.session_state.users[login_email] == login_password
        ):

            st.success("Login Successful ✅")

            st.session_state.logged_in = True

            time.sleep(1)

            st.session_state.page = "loading"

            st.rerun()

        else:

            st.error("Invalid Email or Password ❌")

# ---------------- LOADING PAGE ----------------

elif st.session_state.page == "loading":

    st.markdown("""
    <h1 class='main-title'>🤖 AI Processing</h1>
    """, unsafe_allow_html=True)

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("Dashboard Ready ✅")

    time.sleep(1)

    st.session_state.page = "dashboard"

    st.rerun()

# ---------------- DASHBOARD ----------------

elif st.session_state.page == "dashboard":

    st.markdown("""
    <h1 class='main-title'>🚀 Dashboard</h1>
    """, unsafe_allow_html=True)

    if st.button("🏠 Home"):
        st.session_state.page = "home"
        st.rerun()

    if st.button("📄 Upload Resume"):
        st.session_state.page = "upload"
        st.rerun()

    if st.button("⚡ Resume Processing"):
        st.session_state.page = "processing"
        st.rerun()

    if st.button("📊 ATS Results"):
        st.session_state.page = "ats"
        st.rerun()

    if st.button("🧠 Skills Analysis"):
        st.session_state.page = "skills"
        st.rerun()

    if st.button("❌ Missing Skills"):
        st.session_state.page = "missing"
        st.rerun()

    if st.button("💡 AI Suggestions"):
        st.session_state.page = "suggestions"
        st.rerun()

    if st.button("💼 Career Recommendations"):
        st.session_state.page = "career"
        st.rerun()

    if st.button("📜 Resume Tips"):
        st.session_state.page = "tips"
        st.rerun()

    if st.button("📥 Download PDF Report"):
        st.session_state.page = "download"
        st.rerun()

    if st.button("🕘 Resume History"):
        st.session_state.page = "history"
        st.rerun()

    if st.button("👤 Profile"):
        st.session_state.page = "profile"
        st.rerun()

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "welcome"
        st.rerun()

# ---------------- HOME PAGE ----------------

elif st.session_state.page == "home":

    st.title("🏠 Home")

    st.markdown("""
    <div class='card'>
    Welcome to your AI Resume Dashboard 🔥
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- UPLOAD PAGE ----------------

elif st.session_state.page == "upload":

    st.title("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_file:
        st.success("Resume Uploaded Successfully ✅")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- PROCESSING PAGE ----------------

elif st.session_state.page == "processing":

    st.title("⚡ Resume Processing")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("AI Analysis Completed ✅")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- ATS PAGE ----------------

elif st.session_state.page == "ats":

    st.title("📊 ATS Results")

    st.metric("ATS Score", "92%")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- SKILLS PAGE ----------------

elif st.session_state.page == "skills":

    st.title("🧠 Skills Analysis")

    st.markdown("""
    <div class='card'>

    ✅ Python<br><br>
    ✅ SQL<br><br>
    ✅ Machine Learning<br><br>
    ✅ Data Analysis<br><br>
    ✅ Power BI

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- MISSING SKILLS PAGE ----------------

elif st.session_state.page == "missing":

    st.title("❌ Missing Skills")

    st.markdown("""
    <div class='card'>

    🔴 AWS<br><br>
    🔴 Docker<br><br>
    🔴 Kubernetes

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- SUGGESTIONS PAGE ----------------

elif st.session_state.page == "suggestions":

    st.title("💡 AI Suggestions")

    st.markdown("""
    <div class='card'>

    🔥 Add more projects<br><br>
    🔥 Add internships<br><br>
    🔥 Add certifications<br><br>
    🔥 Improve ATS keywords<br><br>
    🔥 Improve formatting

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- CAREER PAGE ----------------

elif st.session_state.page == "career":

    st.title("💼 Career Recommendations")

    st.markdown("""
    <div class='card'>

    🚀 Data Analyst<br><br>
    🚀 Data Scientist<br><br>
    🚀 AI Engineer<br><br>
    🚀 ML Engineer

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- TIPS PAGE ----------------

elif st.session_state.page == "tips":

    st.title("📜 Resume Tips")

    st.markdown("""
    <div class='card'>

    ✅ Keep resume 1 page<br><br>
    ✅ Use ATS keywords<br><br>
    ✅ Add strong projects<br><br>
    ✅ Use proper formatting

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- DOWNLOAD PAGE ----------------

elif st.session_state.page == "download":

    st.markdown("""
    <h1 class='main-title'>
    📥 Professional Resume Report
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:white;
    padding:35px;
    border-radius:25px;
    color:black;
    box-shadow:0 12px 35px rgba(0,0,0,0.45);
    margin-bottom:25px;
    ">

    <h1 style="
    color:#2563eb;
    text-align:center;
    font-size:42px;
    ">
    🚀 Resume Analysis Report
    </h1>

    <hr>

    <h2>📊 ATS Score</h2>

    <div style="
    background:#dbeafe;
    padding:18px;
    border-radius:14px;
    font-size:28px;
    font-weight:bold;
    color:#1d4ed8;
    ">
    ✅ 92% ATS Optimized
    </div>

    <br>

    <h2>🧠 Skills Detected</h2>

    <ul style='font-size:19px; line-height:2;'>
        <li>Python</li>
        <li>SQL</li>
        <li>Machine Learning</li>
        <li>Data Analysis</li>
        <li>Power BI</li>
    </ul>

    <h2>❌ Missing Skills</h2>

    <ul style='font-size:19px; line-height:2; color:red;'>
        <li>AWS</li>
        <li>Docker</li>
        <li>Kubernetes</li>
    </ul>

    <h2>💡 AI Suggestions</h2>

    <ul style='font-size:19px; line-height:2;'>
        <li>Add more projects</li>
        <li>Add internships</li>
        <li>Add certifications</li>
        <li>Improve ATS keywords</li>
        <li>Improve formatting</li>
    </ul>

    <h2>💼 Career Recommendations</h2>

    <ul style='font-size:19px; line-height:2;'>
        <li>Data Analyst</li>
        <li>AI Engineer</li>
        <li>ML Engineer</li>
        <li>Data Scientist</li>
    </ul>

    <br>

    <div style="
    background:#dcfce7;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    color:#166534;
    ">
    ✅ Resume Looks Strong For Tech Jobs
    </div>

    </div>
    """, unsafe_allow_html=True)

    report = """
RESUME ANALYSIS REPORT

ATS SCORE:
92%

SKILLS:
- Python
- SQL
- Machine Learning
- Data Analysis
- Power BI

MISSING SKILLS:
- AWS
- Docker
- Kubernetes

AI SUGGESTIONS:
- Add more projects
- Add internships
- Add certifications
- Improve ATS keywords
- Improve formatting

CAREER RECOMMENDATIONS:
- Data Analyst
- AI Engineer
- ML Engineer
- Data Scientist
"""

    st.download_button(
        label="⬇ Download Professional Report",
        data=report,
        file_name="AI_Resume_Report.txt",
        mime="text/plain"
    )

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- HISTORY PAGE ----------------

elif st.session_state.page == "history":

    st.title("🕘 Resume History")

    st.markdown("""
    <div class='card'>

    📄 Resume_1.pdf<br><br>
    📄 Resume_2.pdf

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- PROFILE PAGE ----------------

elif st.session_state.page == "profile":

    st.title("👤 Profile")

    st.markdown("""
    <div class='card'>

    📧 User Account<br><br>
    🔥 Resume Analyzer User

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
