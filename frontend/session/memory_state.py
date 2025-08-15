import streamlit as st

def init_chat_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
