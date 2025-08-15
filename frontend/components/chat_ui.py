import streamlit as st

def render_chat_ui():
    st.title("🤖 Basic LLM Chatbot")
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
