export async function sendPrompt(prompt, voiceTranscript = '') {
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, voice_transcript: voiceTranscript }),
  });
  return await res.json();
}
