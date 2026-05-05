import subprocess
import tempfile
import json
import requests

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def analyze_python(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    result = subprocess.run(
        ["pylint", tmp_path, "--output-format=json"],
        capture_output=True,
        text=True
    )

    try:
        issues = json.loads(result.stdout)
    except:
        issues = []

    formatted = []
    for i in issues:
        formatted.append({
            "line": i.get("line"),
            "message": i.get("message"),
            "type": i.get("type")
        })

    score = max(0, 10 - len(formatted) * 0.5)

    return {
        "score": round(score, 2),
        "issues": formatted
    }


def get_ai_suggestions(code: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": f"Explain and improve this Python code:\n{code}"}
        ]
    }

    res = requests.post(url, headers=headers, json=data)

    print("STATUS:", res.status_code)
    print("RAW RESPONSE:", res.text)

    try:
        response_json = res.json()
        return response_json["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI ERROR: {res.text}"