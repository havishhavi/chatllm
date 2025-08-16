from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequestDTO, ChatResponseDTO
from app.services.llm_router import LLMRouter
from app.utils.validators import sanitize_input

router = APIRouter()

@router.post("/", response_model=ChatResponseDTO)
async def chat_handler(payload: ChatRequestDTO):
    message = sanitize_input(payload.message)
    print("📩 Received message:", message)
    print(f"🤖 Selected model: {payload.model}")
    print(f"📚 History count: {len(payload.history)}")

    if not message:
        raise HTTPException(status_code=422, detail="Message is empty or invalid.")

    try:
        llm = LLMRouter(provider=payload.model)
        reply = await llm.get_completion(message=message, history=payload.history)
        return ChatResponseDTO(reply=reply)

    except Exception as e:
        print("❌ Error:", str(e))
        raise HTTPException(status_code=500, detail="Internal server error")
