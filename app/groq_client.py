from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def get_groq_response(model, messages, temperature, max_tokens):
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )


def get_json_response(model, messages, response_format, temperature, max_tokens):
    return client.chat.completions.create(
        model=model,
        messages=messages,
        response_format=response_format,
        temperature=temperature,
        max_tokens=max_tokens,
    )
