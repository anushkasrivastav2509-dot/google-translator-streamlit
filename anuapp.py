import streamlit as st
import googletrans
translator = googletrans.Translator()

def get_key(val):
    for key, value in googletrans.LANGUAGES.items():
         if val == value:
             return key
    return "en"

st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
st.title('Text Translator')
option = st.selectbox('Select the language', tuple(googletrans.LANGUAGES.values()))
text = st.text_area('Enter the text to translate')

if text:
    try:
        translated = translator.translate(text, dest=get_key(option))
        st.write('Translated text:', translated.text)
    except Exception as e:
        st.error(f"Translation failed: {e}")
else:
    st.info('Enter text above to get a translation.')
    