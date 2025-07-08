import streamlit as st
import requests

st.set_page_config(page_title="Secure Notes", page_icon="📝")
st.title("🔐 Secure Notes App")

API_URL = "http://localhost:8000"

# --- LOGIN SECTION ---
if "token" not in st.session_state:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            response = requests.post(f"{API_URL}/login", json={
                "username": username,
                "password": password
            })

            if response.status_code == 200:
                st.session_state.token = response.json()["access_token"]
                st.success("✅ Logged in successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Backend not running. Start FastAPI server at localhost:8000")

# --- SECURE NOTES SECTION ---
else:
    st.success("✅ Welcome! You are logged in.")
    st.subheader("📄 Your Notes")

    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    # --- Create New Note ---
    st.markdown("### ➕ Add a New Note")
    note_title = st.text_input("Title", key="new_note_title")
    note_content = st.text_area("Content", key="new_note_content")
    if st.button("Add Note"):
        if note_title and note_content:
            res = requests.post(f"{API_URL}/notes", headers=headers, json={
                "title": note_title,
                "content": note_content
            })
            if res.status_code == 200:
                st.success("✅ Note added successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to add note")
        else:
            st.warning("⚠️ Title and content are required.")

    # --- View Notes ---
    st.markdown("### 📋 Saved Notes")
    try:
        res = requests.get(f"{API_URL}/notes", headers=headers)
        if res.status_code == 200:
            notes = res.json()
            if notes:
                for note in notes:
                    with st.expander(f"📝 {note['title']} (ID: {note['id']})"):
                        st.write(note["content"])
            else:
                st.info("You have no notes yet.")
        elif res.status_code == 401:
            st.error("🔒 Unauthorized. Please login again.")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Backend not running.")

    # --- Logout ---
    if st.button("Logout"):
        del st.session_state.token
        st.rerun()
