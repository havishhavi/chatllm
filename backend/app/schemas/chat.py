from pydantic import BaseModel
from typing import List, Literal, Dict

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str
class ChatRequestDTO(BaseModel):
    message: str
    model: str
    history: List[Dict[str, str]] = []   

class ChatResponseDTO(BaseModel):
    reply: str
