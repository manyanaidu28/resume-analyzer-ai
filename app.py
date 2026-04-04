import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="Resume Analyzer AI", page_icon="🚀")

# Title
st.title("🚀 Resume Analyzer AI")
st.markdown("### Analyze your resume and improve your skills")

st.divider()
st.info("📄 Upload PDF or paste resume for better analysis")

# Skills list
skills = ["python", "sql", "machine learning", "excel", "communication", "data analysis"]

# File Upload
uploaded_file = st.file_uploader("📤 Upload your resume (PDF or TXT)", type=["pdf", "txt"])

resume = ""

# Read uploaded file
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

# Text input option
resume_input = st.text_area("✍️ Or paste your resume here")
if resume_input:
    resume = resume_input

# Analyze button
if st.button("🔍 Analyze"):

    if resume.strip() == "":
        st.warning("⚠️ Please paste or upload your resume first!")

    else:
        resume = resume.lower()

        # Skill detection
        found_skills = [s for s in skills if s in resume]
        missing_skills = [s for s in skills if s not in resume]

        # Score
        score = int((len(found_skills) / len(skills)) * 100) if skills else 0

        # Results
        st.divider()
        st.header("📊 Analysis Report")

        st.success(f"✅ Detected Skills: {', '.join(found_skills) if found_skills else 'None'}")
        st.error(f"❌ Missing Skills: {', '.join(missing_skills) if missing_skills else 'None'}")
        st.metric("📈 Resume Score", f"{score}%")

        # Progress bar
        st.progress(score)

        # Feedback
        if score >= 80:
            st.success("🔥 Excellent Resume")
        elif score >= 50:
            st.warning("⚡ Average Resume")
        else:
            st.error("❗ Improve your resume")

        # Suggestions
        if missing_skills:
            st.warning("💡 Suggested Skills to Learn:")
            for skill in missing_skills:
                st.write(f"👉 {skill.upper()}")
        else:
            st.success("🔥 Your resume is strong! Keep it up 💪")

        # Chart
        data = {
            "Type": ["Found Skills", "Missing Skills"],
            "Count": [len(found_skills), len(missing_skills)]
        }

        df = pd.DataFrame(data)
        st.bar_chart(df.set_index("Type"))
