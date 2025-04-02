import streamlit as st

st.set_page_config(page_title="Aprender ingles", page_icon="", layout="wide")

pages = {
    "Gramáticas": [
        st.Page("segments/questions.py", title="Repaso preguntas", icon=":material/contract:"),
    ],
    "Vocabulario": [
        st.Page("segments/vocab.py", title="Sustantivos", icon=":material/barcode:"),
    ], 
}

pg = st.navigation(pages)
pg.run()

