import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Translator App", page_icon="🌍")

st.title("🌍 Language Translator App")
st.write("Translate text between multiple languages instantly")

text = st.text_area("Enter text")

languages = {
    "Hindi": "hi",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "Telugu": "te"
}

target_lang = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source="auto",
            target=languages[target_lang]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter text")
