import os
import time
from app.services.llm_client import OpenAIClient  # you can add GeminiClient later
from app.services.gemini_client import GeminiClient
from app.services.grok_client import GrokClient 
from app.logger import logger 


#Saperation of Concerns
#easier to update the logic without tiuching other logics
#easy testing and debugging
class LLMRouter:
    def __init__(self, provider: str = None):
        # Allow dynamic override or fallback to env
        self.provider = (provider or os.getenv("LLM_PROVIDER", "openai")).lower()

        logger.info(f"🔁 LLMRouter initialized with provider: {self.provider}")

        if self.provider == "openai":
            self.client = OpenAIClient()
        elif self.provider == "gemini":
            self.client = GeminiClient()
        elif self.provider == "grok":
            self.client = GrokClient()
        else:
            logger.error(f"❌ Unsupported LLM provider: {self.provider}")
            raise ValueError(f"Unsupported LLM provider: {self.provider}")
    async def get_completion(self, message: str, history: list) -> str:
        return await self.client.get_completion(message=message, history=history)


