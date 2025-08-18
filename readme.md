# 🤖 Basic LLM Chatbot

A simple, modular chatbot built using **FastAPI**, **OpenAI**, and **Streamlit**. The system allows users to input messages via a web UI, processes them through a backend API, and returns responses from an LLM (e.g., GPT-3.5-turbo).

---

## 🚀 Features

- 🔄 **Multi-LLM Support**: Switch between `OpenAI`, `Gemini`, and `Grok` seamlessly.
- 💬 **Streamlit UI**: Responsive, chat-style interface with selectable model and session.
- 🧠 **Chat History**: Automatically saves user sessions to JSON and allows reloading conversations.
- 🔒 **Rate Limiting**: Prevent abuse with per-session request throttling (configurable).
- ⚙️ **FastAPI Backend**: Async-powered LLM request handling with centralized logging.
- 📊 **HTML Test Reports**: Run tests and generate beautiful reports using `pytest-html`.
- 🧹 **Code Quality**: Pylint scan support to enforce clean, readable code.

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




Chat History
Each session is stored in /backend/app/history/{session_id}.json.

Frontend allows loading previous sessions via dropdown.

You can view history via:

/history/sessions – list session IDs

/history/{session_id} – fetch chat log

🧃 Rate Limiting
Default: 5 requests per 60 seconds per session

Configurable in: backend/app/utils/rate_limit.py

Returns 429 on exceeding the limit

👨‍💻 Author
Built with ❤️ by @havishhavi