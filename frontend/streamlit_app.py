import streamlit as st
import uuid
import requests
from services.api_client import get_llm_response
from session.memory_state import init_chat_session
from utils.feedback import render_error
from components.chat_ui import render_chat_ui

BACKEND_URL = "http://localhost:8000"

# --- Page Setup ---
st.set_page_config(page_title="LLM Chatbot", layout="centered")
st.title("🤖 Multi-LLM Chatbot")

# --- LLM Provider Selection ---
model = st.selectbox("Choose LLM provider", ["openai", "gemini", "grok"])

# --- Fetch Available Sessions from Backend ---
@st.cache_data(ttl=30)
def fetch_sessions():
    try:
        res = requests.get(f"{BACKEND_URL}/history/sessions")
        return [s.replace(".json", "") for s in res.json()]
    except:
        return []

available_sessions = fetch_sessions()

# --- Session State Setup ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "__backend_history__" not in st.session_state:
    st.session_state["__backend_history__"] = []

# --- Load Previous Session ---
load_prev = st.toggle("🔁 Load Previous Session", value=False)
if load_prev and available_sessions:
    selected = st.selectbox("Choose a session to load", available_sessions)
    if selected and st.session_state.session_id != selected:
        st.session_state.session_id = selected
        res = requests.get(f"{BACKEND_URL}/history/{selected}")
        if res.status_code == 200:
            history = res.json()["history"]
            st.session_state.chat_history = history.copy()
            st.session_state["__backend_history__"] = history.copy()
        st.success(f"✅ Loaded session: `{selected}`")

else:
    # New session
    if st.button("🆕 New Chat"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.chat_history = []
        st.session_state["__backend_history__"] = []
        st.rerun()

# --- Render Chat UI ---
init_chat_session()
render_chat_ui()

# --- Chat Input ---
if prompt := st.chat_input("Send a message"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        try:
            # Append user's current message to prior history
            history_for_backend = st.session_state["__backend_history__"] + [{"role": "user", "content": prompt}]
            reply = get_llm_response(
                prompt,
                model,
                history_for_backend,
                st.session_state.session_id
            )

            # Display reply in UI
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.session_state["__backend_history__"].append({"role": "user", "content": prompt})
            st.session_state["__backend_history__"].append({"role": "assistant", "content": reply})

            with st.chat_message("assistant"):
                st.markdown(f"🧠 **[{model.upper()}]**")
                st.markdown(reply, unsafe_allow_html=True)

        except Exception as e:
            render_error(str(e))
