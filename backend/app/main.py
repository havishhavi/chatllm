import os
from fastapi import FastAPI
from app.router.chat import router as chat_router
from app import config  # this triggers load_dotenv()
from app.middleware.cors_middleware import add_cors
from app.logger import logger  # ✅ Now importing logger from logger.py
from app.router.chat import router as history_router

# ------------------------
# ✅ FastAPI App Setup
# ------------------------
app = FastAPI(title="LLM Chatbot")

add_cors(app)
app.include_router(chat_router, prefix="/chat")
app.include_router(history_router)


# ------------------------
# ✅ Startup Log
# ------------------------
logger.info("🚀 FastAPI app started successfully.")