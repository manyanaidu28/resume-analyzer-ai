# 🔐 Login System
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.title("🔐 Login")

    username = st.text_input("Enter your name")

    if st.button("Login"):
        if username.strip() != "":
            st.session_state.user = username
            st.success(f"Welcome {username} 👋")
            st.rerun()
        else:
            st.warning("Please enter your name")

    st.stop()
else:
    st.sidebar.success(f"👤 Logged in as: {st.session_state.user}")

# 📂 History system
if "history" not in st.session_state:
    st.session_state.history = []
