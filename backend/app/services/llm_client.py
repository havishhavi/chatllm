import os
import httpx

class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def get_completion(self, message: str) -> str:
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
        }
        print("Sending request to OpenAI API with payload:", message)
        print("🔑 Using API key:", self.api_key[:10], "***")  # just log first 10 characters
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload,
                    timeout=10
                )
                print("✅ Response status:", response.status_code)
                print("📥 Response body:", response.text)

                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]

            except httpx.HTTPStatusError as e:
                print("❌ HTTP error:", e.response.status_code, e.response.text)
                raise
            except Exception as e:
                print("❌ General error:", str(e))
                raise
        #async with httpx.AsyncClient() as client:
        #    response = await client.post(self.api_url, headers=self.headers, json=payload, timeout=10)
        #    response.raise_for_status()
        #    return response.json()["choices"][0]["message"]["content"]
