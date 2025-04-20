from gtts import gTTS
import streamlit as st
import os
from io import BytesIO
import pandas as pd

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)    
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    
    return audio_bytes

def load_working_vocab_df():
    df= pd.read_csv("english-vocab.csv",
                    sep=',', skiprows=1, 
                    names=['category','sub-category', 'word', 'type', 'example'], 
                    encoding="utf-8", engine='python', quotechar='"', doublequote=True)
    return df
