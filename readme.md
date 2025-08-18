# 🤖 Basic LLM Chatbot

A simple, modular chatbot built using **FastAPI**, **OpenAI**, and **Streamlit**. The system allows users to input messages via a web UI, processes them through a backend API, and returns responses from an LLM (e.g., GPT-3.5-turbo).

---

## ⚙️ Features

- 🔌 LLM integration via OpenAI API (GPT-3.5-turbo)
- 🧠 Streamlit UI with chat-like interface
- 🛡️ API key security via `.env`
- 🧾 Async FastAPI backend using `httpx`
- 🚀 Clean project structure (backend & frontend separation)
- 🎯 Built-in input sanitization and error handling

python -m venv venv
venv\Scripts\activate
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

cd ../frontend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py

run tests
pytest test/ --html=test/reports/test_report.html --self-contained-html
