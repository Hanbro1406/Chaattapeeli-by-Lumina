# Bilingual Sarcastic Comeback Generator - Flask Backend with Gemini (app.py) - FINAL
import os
import speech_recognition as sr
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import tempfile
import subprocess
import random
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS # 👈 1. IMPORT gTTS
import io             # 👈 2. IMPORT io
import base64         # 👈 3. IMPORT base64

# --- Setup ---
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Load environment variables from .env file
load_dotenv()

# --- Configure Gemini API ---
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash') # Using Flash for speed
    print("Gemini API configured successfully.")
except (AttributeError, KeyError):
    print("🔴 FATAL ERROR: GEMINI_API_KEY not found or invalid. Make sure you have a .env file with the key.")
    model = None # Set model to None if API key is missing

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True


# --- Core Functions ---

# ... (keep your existing convert_audio_to_wav, transcribe_audio_bilingual, 
#      generate_sarcastic_comeback, and get_fallback_response functions exactly as they are) ...

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

    try:
        with sr.AudioFile(wav_path) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)
            
            try:
                print("Attempting transcription in Malayalam...")
                text = recognizer.recognize_google(audio_data, language="ml-IN")
                print(f"Successfully transcribed in Malayalam: '{text}'")
                return text, "ml-IN"
            except sr.UnknownValueError:
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
    finally:
        print("Cleaning up temporary audio files...")
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)


def generate_sarcastic_comeback(user_text, lang):
    """Generates a sarcastic comeback using the Gemini API."""
    if not model:
        print("⚠️ Gemini model not available. Using fallback responses.")
        return get_fallback_response(lang)

    language_name = "Malayalam" if lang == "ml-IN" else "English"
    
    prompt = f"""
    You are 'Chaattapeeli', a witty and extremely sarcastic AI character from Kerala, India.
    Your task is to generate a short, sharp, sarcastic comeback to the user's statement.
    The user's statement is: "{user_text}"
    The comeback MUST be in the {language_name} language.
    Keep it concise and cutting, like a quick retort. Do not add any extra explanations, apologies, or introductory text like "Here is a comeback:". Just provide the raw comeback.
    """
    
    try:
        print(f"Generating Gemini comeback in {language_name} for: '{user_text}'")
        response = model.generate_content(prompt)
        comeback = response.text.strip()
        print(f"Generated comeback: '{comeback}'")
        return comeback
    except Exception as e:
        print(f"🔴 Error calling Gemini API: {e}")
        print("⚠️ Falling back to predefined responses.")
        return get_fallback_response(lang)

def get_fallback_response(lang):
    """Provides a random predefined response if the API fails."""
    malayalam_responses = [
        "ഓ, എന്തൊരു പുതുമ.", "വൗ, ഇത് പറയാനാണോ ഇത്രയും കഷ്ടപ്പെട്ടത്?",
        "ഇതൊക്കെ വലിയ ബുദ്ധിയാണെന്നാണോ വിചാരം?", "ഏതായാലും ശ്രമിച്ചല്ലോ, അതുമതി."
    ]
    english_responses = [
        "Oh, how original.", "Wow, amazing insight. Truly.",
        "Is that supposed to be clever?", "Well, at least you tried."
    ]
    return random.choice(malayalam_responses) if lang == "ml-IN" else random.choice(english_responses)


# --- 👇 4. ADD THIS NEW FUNCTION ---
def generate_audio_response(text, lang):
    """
    Generates audio from text using gTTS and returns it as a base64 encoded string.
    """
    print(f"Generating audio for: '{text}' in lang: {lang.split('-')[0]}")
    try:
        tts = gTTS(text=text, lang=lang.split('-')[0], slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        audio_base64 = base64.b64encode(audio_fp.read()).decode('utf-8')
        return audio_base64
    except Exception as e:
        print(f"🔴 Error generating audio with gTTS: {e}")
        return None


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
        comeback = "I can't even be bothered to reply to that noise."
        detected_lang = "en-US" # Default to English for error messages
    else:
        comeback = generate_sarcastic_comeback(transcribed_text, detected_lang)

    # --- 👇 5. MODIFY THIS SECTION ---
    # Generate the audio response from the comeback text
    audio_response = generate_audio_response(comeback, detected_lang)

    emit('transcription_result', {
        "original_text": transcribed_text,
        "sarcastic_comeback": comeback,
        "lang": detected_lang,
        "audio_response": audio_response # Send the audio data to the frontend
    })
    # --- END OF MODIFICATION ---

# --- Main Execution ---

if __name__ == '__main__':
    print("Starting Bilingual Flask-SocketIO server with Gemini Integration...")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
