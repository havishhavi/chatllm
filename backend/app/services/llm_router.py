import os
from app.services.llm_client import OpenAIClient  # you can add GeminiClient later

class LLMRouter:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "openai").lower()

        if self.provider == "openai":
            self.client = OpenAIClient()
        elif self.provider == "gemini":
            # from app.services.gemini_client import GeminiClient
            # self.client = GeminiClient()
            raise NotImplementedError("Gemini support not yet implemented.")
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")

    async def get_completion(self, prompt: str) -> str:
        return await self.client.get_completion(prompt)
