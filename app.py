import streamlit as st

st.title("📄 Resume Analyzer AI")

skills = ["python", "sql", "machine learning", "excel", "communication", "data analysis"]

resume = st.text_area("Paste your resume here")

if st.button("Analyze"):
    resume = resume.lower()

    found_skills = [s for s in skills if s in resume]
    missing_skills = [s for s in skills if s not in resume]

    score = int((len(found_skills) / len(skills)) * 100)

    st.subheader("Results")
    st.write("Detected Skills:", ", ".join(found_skills))
    st.write("Missing Skills:", ", ".join(missing_skills))
    st.write("Resume Score:", score, "%")

    if missing_skills:
        st.warning("Try learning: " + ", ".join(missing_skills))
    else:
        st.success("Great! Your resume is strong 💪")
