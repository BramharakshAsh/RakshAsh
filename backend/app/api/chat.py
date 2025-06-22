from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.services.llm_adapter import generate_response
from app.services.memory_retriever import get_context
from app.services.memory_tagger import tag_and_store
from app.services.memory_store import save_to_memory

router = APIRouter()

@router.post("/api/chat", response_model=ChatResponse)
def chat_with_rakshash(payload: ChatRequest):
    try:
        project_id = payload.project_id or "default"
        memory = get_context(project_id, payload)
        reply = generate_response(payload.prompt, memory)
        tag_and_store(payload, reply)
        save_to_memory(project_id, {"prompt": payload.prompt, "reply": reply})
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
