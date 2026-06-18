from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://portfolio-chat-bot-two.vercel.app",
    "https://innovatesoftwaresolution.com",
    "https://ashar.innovatesoftwaresolution.com",
    "http://localhost:3000",
    "https://practice-nextjs-iota-one.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)