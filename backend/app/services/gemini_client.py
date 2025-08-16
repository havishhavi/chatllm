import os
import google.generativeai as genai

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing in environment.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    async def get_completion(self, message: str, history: list) -> str:
        # Convert OpenAI-style history to Gemini format
        history_text = ""
        for turn in history:
            prefix = "User" if turn["role"] == "user" else "Assistant"
            history_text += f"{prefix}: {turn['content']}\n"

        full_prompt = f"{history_text}User: {message}\nAssistant:"
        response = self.model.generate_content(full_prompt)
        return response.text
