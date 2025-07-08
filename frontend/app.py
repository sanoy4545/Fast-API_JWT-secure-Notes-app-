import streamlit as st
import requests

st.set_page_config(page_title="Secure Notes", page_icon="📝")
st.title("🔐 Secure Notes App")

# --- LOGIN SECTION ---
if "token" not in st.session_state:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            response = requests.post("http://localhost:8000/login", json={
                "username": username,
                "password": password
            })

            if response.status_code == 200:
                token = response.json()["access_token"]
                st.session_state.token = token
                st.success("✅ Logged in successfully!")
                st.rerun()  # 👈 immediately show next section
            else:
                st.error("❌ Invalid credentials")

        except requests.exceptions.ConnectionError:
            st.error("⚠️ Backend not running. Start FastAPI server at localhost:8000")

# --- NOTES SECTION ---
else:
    st.success("✅ Welcome! You are logged in.")
    st.subheader("Your Notes")

    if st.button("Load Notes"):
        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }
        try:
            res = requests.get("http://localhost:8000/notes", headers=headers)
            if res.status_code == 200:
                notes = res.json()
                st.json(notes)
            elif res.status_code == 401:
                st.error("🔒 Unauthorized: Your token may be expired or invalid.")
            else:
                st.error(f"⚠️ Unexpected error: {res.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Backend not running. Start FastAPI server at localhost:8000")

    if st.button("Logout"):
        del st.session_state.token
        st.rerun()
