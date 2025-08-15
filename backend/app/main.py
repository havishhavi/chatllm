from fastapi import FastAPI
from app.router.chat import router as chat_router
from app import config  # this triggers load_dotenv()

from app.middleware.cors_middleware import add_cors

app = FastAPI(title="LLM Chatbot")

add_cors(app)
app.include_router(chat_router, prefix="/chat")
