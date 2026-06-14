import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Translator Chat",
    page_icon="💬",
    layout="centered"
)

# ---------------- CHATGPT STYLE CSS ----------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #0d1117;
        color: white;
    }

    /* Chat container */
    .chat-box {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    /* User message */
    .user-msg {
        background-color: #1f6feb;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: right;
    }

    /* Bot message */
    .bot-msg {
        background-color: #161b22;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: left;
        border: 1px solid #30363d;
    }

    /* Button */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #2ea043;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.title("💬 AI Translator Chat")
st.write("Chat-style translation powered by AI 🌍")

# ---------------- SESSION ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

languages = {
    "Hindi": "hi",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "Telugu": "te"
}

lang = st.selectbox("Choose Language 🌍", list(languages.keys()))
user_input = st.text_input("Type your message...")

# ---------------- SEND ----------------
if st.button("Send 🚀"):
    if user_input.strip():

        # detect language
        detected = detect(user_input)

        # translate
        translated = GoogleTranslator(
            source="auto",
            target=languages[lang]
        ).translate(user_input)

        # store chat
        st.session_state.chat.append(("user", user_input))
        st.session_state.chat.append(("bot", translated))

# ---------------- DISPLAY CHAT ----------------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"<div class='user-msg'>🧑 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>🤖 {msg}</div>", unsafe_allow_html=True)
