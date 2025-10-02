from flask import Flask, request, send_file
import openai
from pathlib import Path

# Set your API key
openai.api_key = "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"

app = Flask(__name__)

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    text = request.json.get["text"]
    speech_file = Path("output.mp3")
    with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",  # Fast text-to-speech model
        voice="alloy",
        input=text
    ) as response:
        response.stream_to_file(speech_file)
        return send_file(speech_file, as_attachment=True)
    
    if __name__ == '__main__':
        app.run(debug=True)
        
