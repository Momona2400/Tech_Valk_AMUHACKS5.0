import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

def get_ai_response(message):

    payload = {
        "inputs": message,
        "parameters": {
            "max_new_tokens": 100
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        data = response.json()

        if isinstance(data, list):
            return data[0]["generated_text"]

        # If HF returns error
        return smart_fallback(message)

    except Exception:
        return smart_fallback(message)


def smart_fallback(message):
    message = message.lower()

    if any(word in message for word in ["hello", "hey", "hi"]):
        return "Hey! How may I help you?"

    if "confidence" in message:
        return "Confidence grows through action. Take one small bold step today."

    if "interview" in message:
        return "Prepare 3 strong stories about your strengths. Practice them aloud."

    if "fear" in message:
        return "Fear reduces when you face it gradually. Start small."

    return "I believe in your growth. Focus on one small improvement today."
