from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze_python, get_ai_suggestions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/analyze")
def analyze(req: CodeRequest):
    result = analyze_python(req.code)

    try:
        ai = get_ai_suggestions(req.code)
        result["ai"] = ai
    except:
        result["ai"] = "AI not available"

    return result