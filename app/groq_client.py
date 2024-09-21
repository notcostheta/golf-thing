from groq import Groq
from app.config import GROQ_API_KEY


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def create_completion(
        self, model, messages, response_format=None, temperature=0, max_tokens=8000
    ):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            response_format=response_format,
            temperature=temperature,
            max_tokens=max_tokens,
        )
