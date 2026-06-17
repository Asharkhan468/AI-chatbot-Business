from fastapi import APIRouter
from pydantic import BaseModel

from app.services.vector_db import collection
from app.services.gemini_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    client_id: str
    message: str


@router.post("/chat")
def chat(data: ChatRequest):

    result = collection.query(
        query_texts=[data.message],
        n_results=3
    )

    documents = result.get("documents", [[]])

    context = "\n".join(documents[0]) if documents else ""

    prompt = f"""
    You are a business assistant.

    Business Information:
        {context}

        User Question:
            {data.message}

            Answer only from the business information.
            """

    answer = ask_gemini(prompt)

    return {"reply": answer}