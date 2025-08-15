import streamlit as st

def render_spinner(message="Processing..."):
    return st.spinner(message)

def render_error(msg: str):
    st.error(f"⚠️ {msg}")
