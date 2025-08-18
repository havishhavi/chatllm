import os
import google.generativeai as genai
from app.logger import logger 

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing in environment.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    async def get_completion(self, message: str, history: list) -> str:
        logger.info("🟡 [Gemini] Generating response...")

        try:
            # Convert chat history to Gemini-compatible prompt
            history_text = ""
            for turn in history:
                prefix = "User" if turn["role"] == "user" else "Assistant"
                history_text += f"{prefix}: {turn['content']}\n"

            full_prompt = f"{history_text}User: {message}\nAssistant:"
            logger.debug(f"📤 [Gemini] Prompt:\n{full_prompt}")

            response = self.model.generate_content(full_prompt)

            logger.info("✅ [Gemini] Response received.")
            logger.debug(f"📥 [Gemini] Raw Response: {response.text[:300]}...")  # Log first 300 chars only

            return response.text

        except Exception as e:
            logger.exception("❌ [Gemini] Failed to get response.")
            raise
