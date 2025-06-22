import json
from pathlib import Path

MEMORY_FILE = Path(__file__).parent.parent.parent / "memory" / "chat_memory.json"
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text(json.dumps({}))

def load_memory(project_id):
    memory = json.loads(MEMORY_FILE.read_text())
    return memory.get(project_id, [])

def save_to_memory(project_id, entry):
    memory = json.loads(MEMORY_FILE.read_text())
    memory.setdefault(project_id, []).append(entry)
    MEMORY_FILE.write_text(json.dumps(memory, indent=2))
