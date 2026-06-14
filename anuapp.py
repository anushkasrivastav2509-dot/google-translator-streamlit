import streamlit as st
from deep_translator import GoogleTranslator

st.title("Google Translator App")

text = st.text_input("Enter text")

target_lang = st.selectbox("Choose language", ["hi", "fr", "es", "de", "ta", "te"])

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
        st.success(translated)
    
