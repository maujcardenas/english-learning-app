from gtts import gTTS
import streamlit as st
import os
from io import BytesIO

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    
    # For Streamlit deployment
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    
    return audio_bytes

# Streamlit example
st.title("Text to Speech App")
text_input = st.text_area("Enter text to convert to speech:")

if st.button("Convert to Speech") and text_input:
    audio_bytes = text_to_speech(text_input)
    st.audio(audio_bytes, format="audio/mp3")