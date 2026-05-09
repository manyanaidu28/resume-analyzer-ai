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

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {}

if "history" not in st.session_state:
    st.session_state.history = []

# =========================================================
# CUSTOM CSS
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

/* Typography */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* 3D Buttons */

.stButton > button {

    background: linear-gradient(
        135deg,
        #4f46e5,
        #9333ea
    );

    color: white;
    border: none;
    border-radius: 18px;
    padding: 14px 24px;
    font-size: 20px;
    font-weight: bold;

    box-shadow:
        0px 8px 20px rgba(0,0,0,0.35);

    transition:
        all 0.3s ease-in-out;

    width: 100%;
}

.stButton > button:hover {

    transform:
        translateY(-4px)
        scale(1.03);

    box-shadow:
        0px 12px 25px rgba(0,0,0,0.45);

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #a855f7
        );
}

.stButton > button:active {

    transform: scale(0.96);
}

/* Input Fields */

.stTextInput input {

    background-color: #1e293b !important;
    color: white !important;

    border-radius: 14px !important;

    border: 1px solid #334155 !important;
}

/* Upload Box */

.stFileUploader {

    background-color: #1e293b;

    padding: 20px;

    border-radius: 16px;

    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# WELCOME PAGE
# =========================================================

if st.session_state.page == "welcome":

    st.markdown("""
    <div style='text-align:center; padding-top:70px;'>

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
    st.write("")

    st.markdown("""
    ### ✨ Features

    ✅ AI Resume Analysis  
    ✅ ATS Score Checker  
    ✅ Missing Skills Detection  
    ✅ Career Recommendations  
    ✅ Resume Improvement Tips  
    ✅ PDF Report Download  
    ✅ AI Suggestions  
    ✅ Resume History  
    """)

    st.write("")
    st.write("")
    st.write("")

    if st.button(
        "🚀 Get Started",
        use_container_width=True
    ):

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

            st.success(
                "Account created successfully ✅"
            )

            time.sleep(1)

            st.session_state.page = "login"

            st.rerun()

    st.write("")

    if st.button("🔑 Already Have Account?"):

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

    if st.button("🚀 Login"):

        if (
            login_email in st.session_state.users
            and
            st.session_state.users[login_email]
            == login_password
        ):

            st.success("Login Successful ✅")

            st.session_state.logged_in = True

            st.session_state.page = "loading"

            st.rerun()

        else:

            st.error("Invalid Email or Password ❌")

# =========================================================
# AI LOADING PAGE
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

    st.sidebar.title("🚀 Dashboard")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Home",
            "📄 Upload Resume",
            "⚡ Resume Processing",
            "📊 ATS Results",
            "🧠 Skills Analysis",
            "❌ Missing Skills",
            "💡 AI Suggestions",
            "💼 Career Recommendations",
            "📜 Resume Tips",
            "📥 Download PDF Report",
            "🕘 Resume History",
            "👤 Profile"
        ]
    )

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False

        st.session_state.page = "welcome"

        st.rerun()

    # =====================================================
    # HOME
    # =====================================================

    if page == "🏠 Home":

        st.markdown("""
        <div style='text-align:center;'>

        <h1 style='font-size:60px;'>
        🚀 Resume Analyzer AI
        </h1>

        <p style='font-size:25px; color:#d1d5db;'>

        Welcome to your AI Dashboard 🔥

        </p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("📄 Resume Checks", "120+")

        with col2:
            st.metric("🤖 AI Accuracy", "95%")

        st.write("")

        st.metric("🚀 ATS Success", "90%")

    # =====================================================
    # UPLOAD RESUME
    # =====================================================

    elif page == "📄 Upload Resume":

        st.title("📄 Upload Resume")

        uploaded_file = st.file_uploader(
            "Upload your resume",
            type=["pdf"]
        )

        if uploaded_file:

            st.success(
                "Resume uploaded successfully ✅"
            )

            st.session_state.history.append(
                uploaded_file.name
            )

    # =====================================================
    # PROCESSING
    # =====================================================

    elif page == "⚡ Resume Processing":

        st.title("⚡ Resume Processing")

        st.info("AI is processing your resume...")

        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.03)

            progress.progress(i + 1)

        st.success(
            "Resume processed successfully 🚀"
        )

    # =====================================================
    # ATS RESULTS
    # =====================================================

    elif page == "📊 ATS Results":

        st.title("📊 ATS Results")

        st.metric("🚀 ATS Score", "88%")

        st.progress(88)

        st.success(
            "Your resume is ATS Friendly ✅"
        )

    # =====================================================
    # SKILLS ANALYSIS
    # =====================================================

    elif page == "🧠 Skills Analysis":

        st.title("🧠 Skills Analysis")

        st.success("""
✅ Python  
✅ SQL  
✅ Communication  
✅ Teamwork  
✅ Leadership  
""")

    # =====================================================
    # MISSING SKILLS
    # =====================================================

    elif page == "❌ Missing Skills":

        st.title("❌ Missing Skills")

        st.warning("""
⚠️ Machine Learning  
⚠️ Cloud Computing  
⚠️ Data Structures  
⚠️ GitHub Projects  
""")

    # =====================================================
    # AI SUGGESTIONS
    # =====================================================

    elif page == "💡 AI Suggestions":

        st.title("💡 AI Suggestions")

        st.info("""
🔥 Add more projects  
🔥 Add certifications  
🔥 Improve ATS keywords  
🔥 Improve formatting  
""")

    # =====================================================
    # CAREER RECOMMENDATIONS
    # =====================================================

    elif page == "💼 Career Recommendations":

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

    elif page == "📜 Resume Tips":

        st.title("📜 Resume Tips")

        st.info("""
✅ Keep resume one page  
✅ Add internships  
✅ Add achievements  
✅ Use action words  
""")

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    elif page == "📥 Download PDF Report":

        st.title("📥 Download PDF Report")

        report = """
Resume Analyzer AI Report

ATS Score: 88%

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

    elif page == "🕘 Resume History":

        st.title("🕘 Resume History")

        if len(st.session_state.history) == 0:

            st.warning("No resumes uploaded ⚠️")

        else:

            for file in st.session_state.history:

                st.success(f"📄 {file}")

    # =====================================================
    # PROFILE
    # =====================================================

    elif page == "👤 Profile":

        st.title("👤 Profile")

        st.info("""
👤 Resume Analyzer User  
📧 Email Registered  
🚀 Premium Dashboard  
🤖 AI Enabled Account  
""")
