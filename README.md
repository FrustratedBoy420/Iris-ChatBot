# IRIS: OptaNex Help Chatbot

IRIS is the help chatbot for [OptaNex](https://github.com/Heeraljiwnani/Optanex-the-eye-care-package-), an eye-care Progressive Web App. It answers questions about OptaNex features, screening tests, languages, accessibility and account access. It refuses questions that are not about OptaNex.

**Live API:** https://iris-chat-bot.vercel.app

## How it works

- A FastAPI app sends each question to Google Gemini (`gemini-2.5-flash-lite`).
- The system instruction holds a knowledge base of OptaNex facts, FAQs, disclaimers and out-of-scope replies. The model answers only from that data.
- Each request starts a new chat, so the bot does not remember earlier messages.
- The app is deployed on Vercel with `@vercel/python`. `vercel.json` routes every path to `main.py` and sets CORS headers.

## API

| Method | Path | Body | Response |
| :-- | :-- | :-- | :-- |
| `GET` | `/` | none | `{"status": "IRIS Chatbot API is running"}` |
| `GET` | `/welcome` | none | `{"reply": "<welcome message>"}` |
| `POST` | `/chat` | `{"prompt": "How do I upload retinal images?"}` | `{"reply": "<answer>"}` |

## Run locally

```bash
pip install -r requirements.txt
export GEMINI_API_KEY=your-key   # Windows PowerShell: $env:GEMINI_API_KEY="your-key"
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs to try the endpoints.

## Stack

Python, FastAPI, Pydantic, Google Generative AI SDK, Vercel
