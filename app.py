import streamlit as st

st.set_page_config(page_title="Resume Analyzer AI", page_icon="🚀")

st.title("🚀 Resume Analyzer AI")
st.markdown("### Analyze your resume and improve your skills")

skills = ["python", "sql", "machine learning", "excel", "communication", "data analysis"]

resume = st.text_area("📄 Paste your resume here")

if st.button("🔍 Analyze"):

    if resume.strip() == "":
        st.warning("⚠️ Please paste your resume first!")
    else:
        resume = resume.lower()

        found_skills = [s for s in skills if s in resume]
        missing_skills = [s for s in skills if s not in resume]

        score = int((len(found_skills) / len(skills)) * 100)

        st.subheader("📊 Results")

        st.success(f"✅ Detected Skills: {', '.join(found_skills)}")
        st.error(f"❌ Missing Skills: {', '.join(missing_skills)}")
        st.info(f"📈 Resume Score: {score}%")

        if missing_skills:
            st.warning("💡 Suggestion: Learn " + ", ".join(missing_skills))
        else:
            st.success("🔥 Great! Your resume is strong 💪")
