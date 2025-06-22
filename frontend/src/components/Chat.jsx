import { useState } from 'react';
import VoiceInput from './VoiceInput';
import { sendPrompt } from '../services/api';

export default function Chat() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [voiceTranscript, setVoiceTranscript] = useState('');

  const handleSend = async () => {
    const data = await sendPrompt(prompt, voiceTranscript);
    setResponse(data.reply);
    const utterance = new SpeechSynthesisUtterance(data.reply);
    utterance.lang = 'en-IN';
    window.speechSynthesis.speak(utterance);
  };

  return (
    <div className="p-4">
      <VoiceInput onTranscript={setVoiceTranscript} />
      <textarea value={prompt} onChange={e => setPrompt(e.target.value)} className="w-full border p-2" placeholder="Ask RakshAsh..." />
      <button onClick={handleSend} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">Send</button>
      <pre className="mt-4 whitespace-pre-wrap">{response}</pre>
    </div>
