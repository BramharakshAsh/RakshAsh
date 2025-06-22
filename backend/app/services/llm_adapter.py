import os
import requests

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_response(prompt: str, context: str = "") -> str:
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {"role": "system", "parts": [{"text": context}]},
            {"role": "user", "parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=body)
    response.raise_for_status()
    return response.json()['candidates'][0]['content']['parts'][0]['text']
