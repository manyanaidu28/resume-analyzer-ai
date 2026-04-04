import streamlit as st
import json
import os
import streamlit as st

# HIDE STREAMLIT MENU & SHARE BUTTON
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None
    # MENU STATE
if "menu" not in st.session_state:
    st.session_state.menu = "Signup"

# ---------------- USER FILE ----------------
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)

with open("users.json", "r") as f:
    users = json.load(f)

# ---------------- AUTH SYSTEM ----------------
if st.session_state.user is None:

    st.session_state.menu = st.sidebar.radio(
    "Account",
    ["Signup", "Login"],
    index=0 if st.session_state.menu == "Signup" else 1
)

menu = st.session_state.menu

    # -------- SIGNUP --------
    if menu == "Signup":
        st.title("📝 Signup")

        new_email = st.text_input("Email")
        new_password = st.text_input("Password", type="password")

        if st.button("Create Account"):
            if new_email in users:
                st.error("User already exists ❌")
            elif new_email == "" or new_password == "":
                st.warning("Fill all fields ⚠")
            else:
                users[new_email] = new_password
                with open("users.json", "w") as f:
                    json.dump(users, f)

                st.success("Account created ✅ Redirecting...")

                st.session_state.menu = "Login"
                st.rerun()

        st.stop()

    # -------- LOGIN --------
    if menu == "Login":
        st.title("🔐 Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if email in users and users[email] == password:
                st.session_state.user = email
                st.success(f"Welcome {email} 🎉")
                st.rerun()
            else:
                st.error("Invalid credentials ❌")

        st.stop()

# ---------------- AFTER LOGIN ----------------
if st.session_state.user is not None:

    st.sidebar.success(f"👤 Logged in as: {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    # -------- APP UI --------
    st.title("🚀 Resume Analyzer AI")
    st.markdown("### Analyze your resume & improve your skills 💡")

    skills = [
        "python", "sql", "machine learning", "excel",
        "communication", "data analysis", "deep learning",
        "nlp", "power bi", "tableau"
    ]

    uploaded_file = st.file_uploader(
        "📄 Upload Resume (PDF or TXT)", type=["pdf", "txt"]
    )

    resume = ""

    # -------- READ FILE --------
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    resume += text
        else:
            resume = uploaded_file.read().decode("utf-8")

    # -------- TEXT INPUT --------
    resume_input = st.text_area("📋 Or paste your resume here")

    if resume_input:
        resume = resume_input

    # -------- ANALYZE --------
    if st.button("🔍 Analyze Resume"):
        if resume.strip() == "":
            st.warning("⚠ Please upload or paste resume")
        else:
            resume = resume.lower()

            found_skills = [s for s in skills if s in resume]
            missing_skills = [s for s in skills if s not in resume]

            score = int((len(found_skills) / len(skills)) * 100)

            st.subheader("📊 Results")
            st.write(f"✅ Found Skills: {', '.join(found_skills) if found_skills else 'None'}")
            st.write(f"❌ Missing Skills: {', '.join(missing_skills) if missing_skills else 'None'}")
            st.write(f"🎯 Score: {score}%")

            st.progress(score)

            # -------- FEEDBACK --------
            feedback = f"""
🔥 Resume Feedback:

- You have {len(found_skills)} important skills.
- Improve by adding: {', '.join(missing_skills[:3])}
- Try adding projects, internships, and certifications.
"""
            st.info(feedback)

            # -------- HISTORY --------
            if "history" not in st.session_state:
                st.session_state.history = []

            st.session_state.history.append({
                "score": score,
                "skills": found_skills
            })

    # -------- HISTORY DISPLAY --------
    st.sidebar.subheader("📜 Your History")

    if "history" in st.session_state:
        for i, item in enumerate(st.session_state.history):
            st.sidebar.write(f"{i+1}. Score: {item['score']}%")
