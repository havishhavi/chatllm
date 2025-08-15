import streamlit as st
from services.api_client import get_llm_response
from session.memory_state import init_chat_session
from utils.feedback import render_spinner, render_error
from components.chat_ui import render_chat_ui

st.set_page_config(page_title="LLM Chatbot", layout="centered")
init_chat_session()
render_chat_ui()

if prompt := st.chat_input("Send a message"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        try:
            reply = get_llm_response(prompt)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        except Exception as e:
            render_error(str(e))
