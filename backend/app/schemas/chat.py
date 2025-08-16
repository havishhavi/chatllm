from pydantic import BaseModel
from typing import List, Literal

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    
class ChatRequestDTO(BaseModel):
    message: str
    model: Literal["openai", "gemini", "grok"] = "openai"
    history: List[ChatMessage] = []

class ChatResponseDTO(BaseModel):
    reply: str
