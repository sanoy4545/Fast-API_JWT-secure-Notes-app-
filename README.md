# 🔐 Secure Notes App

A full-stack note-taking web app built with:

- 🧠 **FastAPI** backend
- 🔐 **JWT-based authentication**
- 🖼 **Streamlit** frontend
- 💽 **MySQL** with SQLAlchemy ORM

Users can register, log in securely, and perform **full CRUD** (Create, Read, Update, Delete) operations on their personal notes.

---

## 🚀 Features

✅ User Authentication (JWT)  
✅ Login-protected endpoints  
✅ Create, View, Edit, and Delete Notes  
✅ Secure token management  
✅ Modern Streamlit UI

---

## 🛠 Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| 🔙 Backend    | FastAPI, SQLAlchemy, Pydantic |
| 🔐 Auth       | OAuth2PasswordBearer + JWT |
| 🗃 Database   | MySQL          |
| 🖥 Frontend   | Streamlit      |
| 🐍 Language   | Python 3.10+   |

---

## 🧪 How It Works

### 1. User logs in via the Streamlit app  
→ `/login` returns a **JWT access token**  
→ The token is stored in `session_state`

### 2. Token is sent in every request  
→ All `/notes` routes are protected using `Depends(get_user)`  
→ User-specific notes are stored & retrieved via SQLAlchemy

### 3. CRUD operations  
→ `POST /notes`: create  
→ `GET /notes`: view  
→ `PUT /notes/{id}`: update  
→ `DELETE /notes/{id}`: delete

---

## 💻 Setup Instructions

### ⚙️ Backend (FastAPI)

```bash
git clone https://github.com/your-username/secure-notes-app.git
cd secure-notes-app/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Create `.env` file with DB and JWT secret
touch .env
```

**Example `.env`:**

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/secure_notes
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

```bash
# Run the FastAPI server
uvicorn main:app --reload
```

---

### 🖥 Frontend (Streamlit)

```bash
cd ../frontend

# Install Streamlit
pip install streamlit requests

# Run the app
streamlit run app.py
```

---

## 📦 Folder Structure

```
secure-notes-app/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── db/
│   ├── schemas.py
│   ├── core/
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
└── README.md
```

---

## 🔐 Security Notes

- JWT is stored only in memory (`st.session_state`) and sent via `Authorization: Bearer` header
- All protected endpoints validate tokens with expiry
- User-specific notes are isolated using `user_id`

---

## 📬 Contact

Made by [Sanoy Boby](https://github.com/sanoyboby)  
📧 sanoyboby924@gmail.com  
📍 Rajagiri School of Engineering and Technology

---

## 📜 License

MIT License. See `LICENSE` file for details.
