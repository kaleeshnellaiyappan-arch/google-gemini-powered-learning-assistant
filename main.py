from fastapi import FastAPI

app = FastAPI(title="EduGenie")

GEMINI_MODEL = "Gemini 1.5 Pro"
LOCAL_MODEL = "LaMini-Flan-T5-783M"

@app.get("/")
def home():
    return {
        "project": "EduGenie",
        "gemini_model": GEMINI_MODEL,
        "local_model": LOCAL_MODEL
    }
