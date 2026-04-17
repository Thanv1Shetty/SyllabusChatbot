import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Syllabus Chatbot", page_icon="🎓", layout="centered")

# -------------------- NEW UI DESIGN --------------------


st.markdown("""
<style>

/* Background - dark smooth gradient */
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e2e8f0;
}

/* Main container */
.block-container {
    padding-top: 2rem;
}

/* User message */
.user-msg {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    padding: 12px 18px;
    border-radius: 20px;
    max-width: 70%;
    margin-left: auto;
    margin-top: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

/* Bot message */
.bot-msg {
    background: #1e293b;
    color: #e2e8f0;
    padding: 12px 18px;
    border-radius: 20px;
    max-width: 70%;
    margin-right: auto;
    margin-top: 10px;
    border: 1px solid #334155;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* Input box */
.stTextInput input {
    border-radius: 25px;
    padding: 14px;
    border: 1px solid #475569;
    background-color: #020617;
    color: white;
}

/* Buttons */
.stButton button {
    border-radius: 25px;
    height: 3em;
    font-weight: 600;
    border: none;
    background: linear-gradient(135deg, #06b6d4, #7c3aed);
    color: white;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.05);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #38bdf8;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)



# -------------------- SIDEBAR --------------------
st.sidebar.title("🎓 Menu")
year = st.sidebar.radio("Choose Year", [1, 2, 3, 4])
st.sidebar.write("Ask anything about your syllabus 💡")

# -------------------- LOAD SYLLABUS --------------------
def load_syllabus(year):
    if year == 1:
        return """
        Subjects:
        - Mathematics
        - Physics
        - Basic Programming
        - Engineering Chemistry
        """
    elif year == 2:
        return """
        Subjects:
        - Data Structures
        - DBMS
        - Operating Systems
        - Computer Organization
        """
    elif year == 3:
        return """
        Subjects:
        - Machine Learning
        - Computer Networks
        - Software Engineering
        - Web Technologies
        """
    elif year == 4:
        return """
        Subjects:
        - Artificial Intelligence
        - Cloud Computing
        - Big Data
        - Final Year Project
        """

# -------------------- PROMPT --------------------
def create_prompt(question, syllabus):
    return f"""
Answer the question briefly using the syllabus.

Syllabus:
{syllabus}

Question:
{question}

Short Answer:
"""

# -------------------- LLM --------------------
def ask_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 150}
            },
            timeout=60
        )
        return response.json().get("response", "No response")
    except Exception as e:
        return f"Error: {e}"

# -------------------- TITLE --------------------
st.markdown('<div class="title">🎓 Smart Academic Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything about your syllabus 📚</div>', unsafe_allow_html=True)

# -------------------- SESSION STATE (CHAT HISTORY) --------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# -------------------- INPUT --------------------
question = st.text_input("Type your question...")

col1, col2 = st.columns([3,1])

with col1:
    ask = st.button("Ask")

with col2:
    clear = st.button("Clear")

# -------------------- HANDLE RESPONSE --------------------
if ask and question:
    syllabus = load_syllabus(year)
    prompt = create_prompt(question, syllabus)

    with st.spinner("Thinking... 🤖"):
        answer = ask_llm(prompt)

    st.session_state.chat.append(("user", question))
    st.session_state.chat.append(("bot", answer))

# -------------------- DISPLAY CHAT --------------------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">🤖 {msg}</div>', unsafe_allow_html=True)

# -------------------- CLEAR --------------------
if clear:
    st.session_state.chat = []
    st.experimental_rerun()