import { useEffect } from 'react';

export default function VoiceInput({ onTranscript }) {
  useEffect(() => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = 'en-IN';
    recognition.interimResults = false;
    recognition.onresult = event => {
      onTranscript(event.results[0][0].transcript);
    };
    document.getElementById('start-voice').onclick = () => recognition.start();
    document.getElementById('stop-voice').onclick = () => recognition.stop();
  }, [onTranscript]);

  return (
    <div className="flex space-x-2">
      <button id="start-voice" className="bg-green-500 text-white px-2">🎙 Start</button>
      <button id="stop-voice" className="bg-red-500 text-white px-2">🛑 Stop</button>
    </div>
