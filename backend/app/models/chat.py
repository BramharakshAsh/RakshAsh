from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    prompt: str
    project_id: Optional[str] = None
    voice_transcript: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
