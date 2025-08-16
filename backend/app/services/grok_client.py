import os
import httpx

class GrokClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "deepseek-coder"  # ✅ or change to mixtral/llama3/gemma
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def get_completion(self, message: str, history: list) -> str:
        # Convert history to OpenAI format
        messages = history.copy()
        messages.append({"role": "user", "content": message})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=10
            )

            print("🟡 GROQ response:", response.status_code)
            print("📥", response.text)
            response.raise_for_status()

            return response.json()["choices"][0]["message"]["content"]
