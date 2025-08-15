from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequestDTO, ChatResponseDTO
from app.services.llm_router import LLMRouter


from app.utils.validators import sanitize_input

router = APIRouter()

@router.post("/", response_model=ChatResponseDTO)
async def chat_handler(payload: ChatRequestDTO):
    message = sanitize_input(payload.message)
    print("Received message:", message)
    if not message:
        raise HTTPException(status_code=422, detail="Message is empty or invalid.")

    llm = LLMRouter()
    try:
        response = await llm.get_completion(message)
        return ChatResponseDTO(reply=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
