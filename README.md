# lumina
<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# [Chaattapeeli] 🎯


## Basic Details
### Team Name: [Lumina]


### Team Members
- Team Lead: [Hansel T Jaison] - [Albertian Institute of Science & Technology]
- Member 2: [Sivani N.S] - [Albertian Institute of Science & Technology]

### Project Description
Chaattapeeli (ചാട്ടപ്പീലി), which translates to "Whip," is a web-based, voice-interactive AI companion. It features an animated character who listens to a user's spoken input in either Malayalam or English. The application then leverages a generative AI to provide a witty, sarcastic comeback in the same language, delivering the response as both text within a modal and as synthesized audio.

### The Problem (that doesn't exist)
In a world filled with overly polite and relentlessly helpful AI assistants, there's a glaring void for a digital companion that doesn't just serve but judges. Users are drowning in a sea of "Certainly, how can I help you?". They secretly yearn for an AI that listens to their deepest thoughts and responds with the sharp, witty, and lovingly sarcastic retort they truly deserve.

### The Solution (that nobody asked for)
Enter Chaattapeeli, the digital embodiment of a quintessential Keralite aunt with a sharp tongue and a heart of... well, something. This application provides the vital service of taking your spoken words, transcribing them, and using the powerful Gemini AI to generate a fittingly sarcastic comeback. It then speaks the response back to you, all while an animated character visibly judges your life choices.

## Technical Details
### Technologies/Components Used
For Software:
- [Languages used: Python, JavaScript, HTML, CSS]
- [Frameworks used: Flask, Flask-SocketIO]
- [Libraries used Key Libraries Used:
Backend: google-generativeai, speech_recognition, gTTS, python-dotenv
Frontend: socket.io-client
External APIs: Google Gemini 1.5 Flash, Google Speech Recognition
- [ffmpeg for audio format conversion]

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:
# Installation
[commands]
Installation
Clone the repository and navigate into the directory.
Bash
git clone <your-repository-url>
cd <repository-name>
Create and activate a Python virtual environment.
Bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

On macOS (via Homebrew): brew install ffmpeg

On Debian/Ubuntu: sudo apt update && sudo apt install ffmpeg
# For Windows
python -m venv venv

.\venv\Scripts\activate

Install ffmpeg. This is a crucial dependency for audio processing.

On Windows: Download from the official website and add the bin directory to your system's PATH.

Install the required Python packages.
Bash

pip install Flask Flask-SocketIO google-generativeai SpeechRecognition python-dotenv gTTS

Create an environment file.

Create a file named .env in the root of the project directory.

Add your Google Gemini API key to this file:=
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"


# Run
Start the Flask backend server. Bash python app.py

You should see output indicating the server is running on http://127.0.0.1:5000. Launch the frontend.

Open the index.html file directly in a modern web browser (like Chrome, Firefox, or Edge).

The browser will ask for microphone permission; you must allow it for the application to work.

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1] ([<img width="1621" height="741" alt="listening" src="https://github.com/user-attachments/assets/4efe4f44-978e-4750-876c-b5c68c71ddf4" />])

*Add caption explaining what this shows*

![Screenshot2]([<img width="1596" height="749" alt="procsessing" src="https://github.com/user-attachments/assets/2977c4a8-3a13-4cee-8b4c-c3f2d661c763" />]
*Add caption explaining what this shows*

![Screenshot3](<img width="1615" height="746" alt="reply" src="https://github.com/user-attachments/assets/ada89cab-c50f-4321-b314-39ed29e2a76c" />
)]
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)


