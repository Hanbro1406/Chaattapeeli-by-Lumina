# Bilingual Sarcastic Comeback Generator - Flask Backend (app.py)
import os
import speech_recognition as sr
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import tempfile
import subprocess
import random

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True

# --- Core Functions ---

def convert_audio_to_wav(input_path, output_path):
    """Converts audio file to WAV format using ffmpeg."""
    try:
        subprocess.run([
            'ffmpeg', '-i', input_path, '-acodec', 'pcm_s16le',
            '-ar', '16000', '-ac', '1', output_path, '-y'
        ], capture_output=True, text=True, check=True)
        return True
    except Exception as e:
        print(f"Error converting audio: {e}")
        return False

def transcribe_audio_bilingual(audio_file_path):
    """
    Tries to transcribe audio in Malayalam first, then falls back to English.
    Returns the transcribed text and the detected language.
    """
    wav_path = "temp_converted.wav"
    if not convert_audio_to_wav(audio_file_path, wav_path):
        return "Audio conversion failed.", "en-US"

    with sr.AudioFile(wav_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio_data = recognizer.record(source)
        
        try:
            # --- 1. First, try to recognize as Malayalam ---
            print("Attempting transcription in Malayalam...")
            text = recognizer.recognize_google(audio_data, language="ml-IN")
            print(f"Successfully transcribed in Malayalam: '{text}'")
            return text, "ml-IN"
        except sr.UnknownValueError:
            # --- 2. If Malayalam fails, try English ---
            print("Malayalam recognition failed, trying English...")
            try:
                text = recognizer.recognize_google(audio_data, language="en-US")
                print(f"Successfully transcribed in English: '{text}'")
                return text, "en-US"
            except sr.UnknownValueError:
                print("Could not understand the audio in either language.")
                return "I couldn't understand what you said.", "en-US"
            except sr.RequestError as e:
                return f"API error: {e}", "en-US"

    # Cleanup temporary files
    if os.path.exists(audio_file_path): os.remove(audio_file_path)
    if os.path.exists(wav_path): os.remove(wav_path)


def generate_sarcastic_comeback(lang):
    """Generates a sarcastic comeback in the detected language."""
    malayalam_responses = [
        "ഓ, എന്തൊരു പുതുമ.", "വൗ, ഇത് പറയാനാണോ ഇത്രയും കഷ്ടപ്പെട്ടത്?",
        "ഇതൊക്കെ വലിയ ബുദ്ധിയാണെന്നാണോ വിചാരം?", "ഏതായാലും ശ്രമിച്ചല്ലോ, അതുമതി."
    ]
    english_responses = [
        "Oh, how original. I'm sure that took you all day.",
        "Wow, that's the best you could come up with? I'm disappointed.",
        "Is that supposed to be clever? Because it's not working.",
        "Well, at least you tried. That's something, I guess."
    ]
    
    if lang == "ml-IN":
        comeback = random.choice(malayalam_responses)
    else:
        comeback = random.choice(english_responses)
        
    print(f"Generated comeback in {lang}: '{comeback}'")
    return comeback

# --- WebSocket Event Handlers ---

@socketio.on('connect')
def handle_connect():
    print(f"Client connected: {request.sid}")

@socketio.on('audio_chunk')
def handle_audio_chunk(audio_data):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_audio_file:
        temp_audio_path = temp_audio_file.name
        temp_audio_file.write(audio_data)

    transcribed_text, detected_lang = transcribe_audio_bilingual(temp_audio_path)
    
    if "couldn't understand" in transcribed_text or "failed" in transcribed_text:
        comeback = "I can't even be bothered to reply to that mess."
        detected_lang = "en-US" # Default to English for error messages
    else:
        comeback = generate_sarcastic_comeback(detected_lang)

    emit('transcription_result', {
        "original_text": transcribed_text,
        "sarcastic_comeback": comeback,
        "lang": detected_lang # <-- NEW: Send detected language to the frontend
    })

# --- Main Execution ---

if __name__ == '__main__':
    print("Starting Bilingual Flask-SocketIO server...")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)