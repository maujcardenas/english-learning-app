import streamlit as st

st.set_page_config(page_title="Aprender ingles", page_icon="", layout="wide")

pages = {
    "Grammar": [
        st.Page("segments/grammar/tense_present_simple.py", title="Simple present tense", icon=":material/mitre:"),
        st.Page("segments/grammar/tense_past_simple.py", title="Simple past tense", icon=":material/mitre:"),
        st.Page("segments/grammar/tense_present_continuous.py", title="Present continuous tense", icon=":material/mitre:"),
        st.Page("segments/grammar/tense_past_continuous.py", title="Past cotinuous tense", icon=":material/mitre:"),
        st.Page("segments/grammar/tense_future_simple.py", title="Future simple tense", icon=":material/mitre:"),
        st.Page("segments/grammar/possesive_adjectives.py", title="Possesive adjectives", icon=":material/mitre:"),
        st.Page("segments/grammar/wh_questions.py", title="Wh- questions", icon=":material/mitre:"),
    ],
    "Vocabulary": [
        st.Page("segments/vocabulary/vocab.py", title="Vocabulary", icon=":material/dictionary:"),
    ], 
}

pg = st.navigation(pages)
pg.run()

