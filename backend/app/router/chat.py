from fastapi import APIRouter, HTTPException, Request
from app.schemas.chat import ChatRequestDTO, ChatResponseDTO
from app.services.llm_router import LLMRouter
from app.utils.validators import sanitize_input
from app.logger import logger
from uuid import uuid4
from app.utils.rate_limit import check_rate_limit  # ✅ Rate limiter
from app.services.history import load_history, save_to_history, list_all_histories  # ✅ Chat history

router = APIRouter()

@router.post("/", response_model=ChatResponseDTO)
async def chat_handler(request: Request, payload: ChatRequestDTO):
    message = sanitize_input(payload.message)
    model = payload.model or "openai"
    #session_id = request.headers.get("X-Session-ID", request.client.host)
    session_id = (
        request.headers.get("X-Session-ID")
        or (getattr(request.client, "host", None) if getattr(request, "client", None) else None)
        or str(uuid4())
    )
    history = payload.history or load_history(session_id)

    logger.info(f"📨 Received message: '{message}' | model={model}")

    if not message:
        logger.warning("⚠️ Empty or invalid message received.")
        raise HTTPException(status_code=422, detail="Message is empty or invalid.")

    # ✅ Rate limiting check
    check_rate_limit(session_id)
    # if not check_rate_limit(session_id):
    #     logger.warning(f"🚫 Rate limit exceeded for session: {session_id}")
    #     raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")

    

    try:
        llm = LLMRouter(provider=model)
        response = await llm.get_completion(message=message, history=history)
        logger.info(f"✅ [{model.upper()}] Response generated successfully.")

        # ✅ Save chat to history
        save_to_history(session_id, {"role": "user", "content": message})
        save_to_history(session_id, {"role": "assistant", "content": response})

        return ChatResponseDTO(reply=response)

    except HTTPException as e:
        logger.error(f"❌ HTTPException: {e.detail}")
        raise e

    except ValueError as ve:
        logger.warning(f"❗ Invalid model error: {ve}")
        msg = str(ve)
        if "Unsupported LLM provider" in msg:
            # match the test expectation
            raise HTTPException(status_code=500, detail=msg)
        else:
            raise HTTPException(status_code=422, detail=msg)
            # raise HTTPException(status_code=422, detail=str(ve))

    except Exception as e:
        logger.exception("💥 Unexpected server error.")
        raise HTTPException(status_code=500, detail="Internal server error.")

@router.get("/history/sessions")
def get_sessions():
    return list_all_histories()

@router.get("/history/{session_id}")
def get_chat_history(session_id: str):
    try:
        history = load_history(session_id)
        if not history:
            raise HTTPException(status_code=404, detail="Session history not found")
        return {"session_id": session_id, "history": history}
    except Exception:
        raise HTTPException(status_code=404, detail="Session history not found")
    
# @router.get("/history/sessions")
# def list_sessions():
#     try:
#         return list_all_histories()
#     except Exception:
#         raise HTTPException(status_code=500, detail="Unable to list sessions")