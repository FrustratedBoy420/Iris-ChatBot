import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Setup: Frontend se connect karne ke liye zaroori hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini Config: Environment variable ka naam pass karein, asli key nahi
GEMINI_API_KEY = os.getenv("AIzaSyAlKE-yc4Oo1yifBNw9qO_6GRv9Nithnw0")
genai.configure(api_key=GEMINI_API_KEY)

# Aapka OptaNex specific instruction
SYSTEM_INSTRUCTION = """
(Aapka pura JSON data yaha paste karein jo aapne upar diya tha...)
You are an IRIS chatbot for optanex...
"""

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite", # Ya jo version aap use karna chahte hain
    system_instruction=SYSTEM_INSTRUCTION
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "IRIS Chatbot API is running on Vercel"}

@app.get("/welcome")
async def welcome():
    chat = model.start_chat(history=[])
    response = chat.send_message("Give a short professional welcome message as IRIS.")
    return {"reply": response.text}

@app.post("/chat")
async def get_response(request: ChatRequest):
    chat = model.start_chat(history=[])
    response = chat.send_message(request.prompt)
    return {"reply": response.text}

