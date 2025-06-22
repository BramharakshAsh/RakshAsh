from app.services.memory_store import load_memory

def get_context(project_id, payload):
    entries = load_memory(project_id)
    context = ""
    for m in entries[-5:]:
        context += f"You: {m['prompt']}\nRakshAsh: {m['reply']}\n"
    if payload.voice_transcript:
        context += f"Voice: {payload.voice_transcript}\n"
    return context
