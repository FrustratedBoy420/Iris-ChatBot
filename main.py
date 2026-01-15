import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variable ka naam 'GEMINI_API_KEY' hona chahiye
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = """... Aapka OptaNex JSON Data ..."""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    system_instruction=SYSTEM_INSTRUCTION
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "IRIS Chatbot is live"}

@app.post("/chat")
async def get_response(request: ChatRequest):
    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(request.prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"reply": f"Internal Error: {str(e)}"}
