import streamlit as st
import utils as ut




text = "I have the dream of recruiting people for my investment company. I would like to use an investment fund of 1000 dollars. Do you know any company that is available for help?"

if st.button("Generate Speech"):
    speech_file = ut.generate_speech_file(text, rate=100)
    st.audio(speech_file)