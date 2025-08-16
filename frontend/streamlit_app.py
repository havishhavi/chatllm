import streamlit as st
from services.api_client import get_llm_response
from session.memory_state import init_chat_session
from utils.feedback import render_error
from components.chat_ui import render_chat_ui

# --- Setup ---
st.set_page_config(page_title="LLM Chatbot", layout="centered")
st.title("🤖 Multi-LLM Chatbot")

# --- LLM Provider Selector ---
model = st.selectbox("Choose LLM provider", ["openai", "gemini", "grok"])

# --- Initialize Session State ---
init_chat_session()

# --- Render Chat History ---
render_chat_ui()

# --- Chat Input ---
if prompt := st.chat_input("Send a message"):
    # Save user input
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to backend and render response
    with st.spinner("Thinking..."):
        try:
            reply = get_llm_response(prompt, model, st.session_state.chat_history)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(f"🧠 **[{model.upper()}]**: {reply}")
        except Exception as e:
            render_error(str(e))
