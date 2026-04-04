import streamlit as st
import pandas as pd
# ---------------- LOGIN SYSTEM ----------------
if "user" not in st.session_state:
    st.session_state.user = None

# Demo users
users = {
    "admin@gmail.com": "1234",
    "user@gmail.com": "1234"
}

if st.session_state.user is None:
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in users and users[email] == password:
            st.session_state.user = email
            st.success(f"Welcome {email} 🚀")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.stop()
    # ---------------- SIDEBAR ----------------
st.sidebar.success(f"👤 Logged in as: {st.session_state.user}")

if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()

# ---------------- HISTORY INIT ----------------
if "history" not in st.session_state:
    st.session_state.history = {}

# ---------------- TITLE ----------------
st.title("🚀 Resume Analyzer AI")
st.markdown("### Analyze your resume & improve your skills 💡")

# ---------------- SKILLS ----------------
skills = [
    "python", "sql", "machine learning", "excel",
    "communication", "data analysis", "deep learning",
    "nlp", "power bi", "tableau"
]

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📂 Upload Resume (PDF or TXT)", type=["pdf", "txt"])

resume = ""

# ---------------- READ FILE ----------------
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

# ---------------- TEXT INPUT ----------------
resume_input = st.text_area("📄 Or paste your resume here")

if resume_input:
    resume = resume_input

# ---------------- ANALYZE ----------------
if st.button("🔍 Analyze Resume"):

    if resume.strip() == "":
        st.warning("⚠️ Please upload or paste resume")
    else:
        resume = resume.lower()

        found_skills = [s for s in skills if s in resume]
        missing_skills = [s for s in skills if s not in resume]

        score = int((len(found_skills) / len(skills)) * 100) if skills else 0

        # ---------------- RESULTS ----------------
        st.subheader("📊 Results")
        st.write(f"✅ Found Skills: {', '.join(found_skills) if found_skills else 'None'}")
        st.write(f"❌ Missing Skills: {', '.join(missing_skills) if missing_skills else 'None'}")
        st.write(f"📈 Score: {score}%")

        st.progress(score)

        # ---------------- SAVE HISTORY ----------------
        user = st.session_state.user

        if user not in st.session_state.history:
            st.session_state.history[user] = []

        st.session_state.history[user].append({
            "score": score,
            "skills": found_skills
        })
# ---------------- SHOW HISTORY ----------------
st.sidebar.subheader("📜 Your History")

user = st.session_state.user

if user in st.session_state.history:
    for i, item in enumerate(st.session_state.history[user][::-1]):
        st.sidebar.write(f"{i+1}. Score: {item['score']}%")
