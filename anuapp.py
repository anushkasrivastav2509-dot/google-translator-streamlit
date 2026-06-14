import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
import base64
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Translator Pro 🌍",
    page_icon="🌍",
    layout="centered"
)

# ---------------- BACKGROUND STYLE ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ffe6f0, #e6f7ff);
    }

    h1 {
        text-align: center;
        color: #ff4d88;
        font-size: 40px;
    }

    .stButton>button {
        background-color: #ff4d88;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
    }

    .block-container {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.title("🌍 AI Translator Pro")
st.write("✨ Translate, Detect Language, and Listen to Output 💖")

# ---------------- INPUT ----------------
text = st.text_area("✍️ Enter text")

languages = {
    "Hindi 🇮🇳": "hi",
    "English 🇬🇧": "en",
    "French 🇫🇷": "fr",
    "Spanish 🇪🇸": "es",
    "German 🇩🇪": "de",
    "Tamil 🇮🇳": "ta",
    "Telugu 🇮🇳": "te"
}

lang_name = st.selectbox("🌍 Choose Language", list(languages.keys()))

# ---------------- SESSION HISTORY ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- TRANSLATE ----------------
if st.button("✨ Translate"):
    if text.strip():

        # detect language
        detected_lang = detect(text)

        # translate
        translated = GoogleTranslator(
            source="auto",
            target=languages[lang_name]
        ).translate(text)

        # show results
        st.success("💖 Translated Text")
        st.write(translated)

        st.info(f"🧠 Detected Language: {detected_lang}")

        # save history
        st.session_state.history.append((text, translated))

        # ---------------- TEXT TO SPEECH ----------------
        tts = gTTS(translated)
        audio_file = "audio.mp3"
        tts.save(audio_file)

        audio_bytes = open(audio_file, "rb").read()
        b64 = base64.b64encode(audio_bytes).decode()

        audio_html = f"""
        <audio controls>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

        os.remove(audio_file)

    else:
        st.warning("⚠️ Please enter text!")

# ---------------- HISTORY SECTION ----------------
st.markdown("---")
st.subheader("📜 Translation History")

for i, (inp, out) in enumerate(reversed(st.session_state.history)):
    st.write(f"**{i+1}.** {inp} ➜ {out}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("💖 Built with Python + Streamlit | AI Translator Pro")
