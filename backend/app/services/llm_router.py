import os
from app.services.llm_client import OpenAIClient  # you can add GeminiClient later
from app.services.gemini_client import GeminiClient
from app.services.grok_client import GrokClient  # Assuming you have a GrokClient implemented


#Saperation of Concerns
#easier to update the logic without tiuching other logics
#easy testing and debugging
class LLMRouter:
    def __init__(self, provider: str = None):
        self.provider = os.getenv("LLM_PROVIDER", "openai").lower()
        #def __init__(self, provider: str = "openai"):
        #self.provider = provider.lower()

        if self.provider == "openai":
            self.client = OpenAIClient()
        elif self.provider == "gemini":
            self.client = GeminiClient()
        elif self.provider == "grok":
            self.client = GrokClient()  # Assuming you have a GrokClient implemented
            
            # from app.services.gemini_client import GeminiClient
            # self.client = GeminiClient()
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")
        #async def get_completion(self, message: str, history: list) -> str:
        #return await self.client.get_completion(message, history)

    #async def get_completion(self, prompt: str, history: list) -> str:
     #   return await self.client.get_completion(prompt, history)
    async def get_completion(self, message: str, history: list) -> str:
        return await self.client.get_completion(message, history)
