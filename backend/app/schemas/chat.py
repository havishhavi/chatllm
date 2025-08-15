from pydantic import BaseModel

class ChatRequestDTO(BaseModel):
    message: str

class ChatResponseDTO(BaseModel):
    reply: str
