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
![Screenshot1](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAOCAYAAABO3B6yAAAHWklEQVR4AQCBAH7/AP/su///7Lz//+y8//7svP/+7L3//uu+//3rvv/967///OrA//zqwf/76sH/++nC//vpw//76cP/+unD//rpw//66cP/++nD//vpw//76cL/++rB//zqwf/86sD//eu///3rvv/+7L3//uy8///svP//7bv//+26///tuv//7br/AIEAfv8A/u27//7tvP/+7bz//u28//3svf/97L7//Oy+//zrv//768D/++vB//vqwv/66sL/+urD//rqw//66sP/+enE//rpw//66sP/+urD//rqwv/76sL/++vB//vrwP/867///Oy+//3svf/97L3//u28//7tu//+7bv//+26///tuv8AgQB+/wD97rz//O68//zuvP/87rz//O69//vtvv/77b//+u2///rswP/67MH/+ezC//nrwv/468P/+OvE//jrxP/468T/+OvE//jrxP/468P/+evD//nrwv/57ML/+uzB//rswP/77b//++2+//ztvf/87r3//e68//3uvP/97rv//e67/wCBAH7/APvwvP/78Lz/+vC8//rwvf/6773/+e++//nvv//47sD/+O7B//fuwf/37cL/9+3D//btxP/27MT/9uzE//bsxf/27MX/9uzE//bsxP/27MT/9+3D//ftwv/47cL/+O3B//nuwP/57r//+u6+//rvvv/6773/+++9//vvvP/777z/AIEAfv8A+PK8//jyvP/48rz/+PK9//fxvv/38b7/9/G///bwwP/28MH/9e/C//Xvw//078T/9O7E//Tuxf/07sX/8+7F//Puxv/07sX/9O7F//Tuxf/07sT/9e7E//Xuw//278L/9u/B//fvwf/38MD/9/C///jwv//48L7/+PC+//jwvv8AgQB+/wD29Lz/9vS8//b0vf/29L3/9fO+//Xzv//08sD/9PLB//Pxwv/z8cP/8vHD//LwxP/y8MX/8e/G//Hvxv/x78b/8e/H//Hvx//x78b/8u/G//Lvxv/y78X/8+/E//PwxP/08MP/9PDC//Xwwv/18cH/9fHA//bxwP/28cD/9vG//wCBAH7/APT1vf/09b3/9PW9//T1vv/z9b//8/S///L0wP/y88H/8fPC//Hyw//w8sT/8PHF//Dxxv/v8Mf/7/DH/+/wyP/v8Mj/7/DI/+/vyP/v78j/8PDH//Dwx//w8Mb/8fDF//Hwxf/y8cT/8vHD//Pxw//z8cL/8/HC//Pxwv/08sH/AIEAfv8A8/a9//P2vf/z9r7/8va+//L1v//x9cD/8fXB//D0wv/w88P/7/PE/+/yxf/u8sb/7vHH/+7xyP/u8cj/7fDJ/+3wyf/t8Mn/7fDJ/+7wyf/u8Mn/7vDI/+/wyP/v8Mf/8PDH//Dwxv/w8cX/8fHF//HxxP/x8cT/8vHE//LxxP8AgQB+/wDy977/8ve+//L2vv/x9r//8fbA//D1wf/w9cL/7/TD/+/0xP/u88X/7vLG/+3yx//t8cj/7fHJ/+zwyv/s8Mr/7PDL/+zvy//s78v/7O/L/+3vy//t78r/7e/K/+7vyf/u8Mn/7/DI/+/wx//w8Mf/8PDG//Dwxv/w8Mb/8PDG/wCBAH7/APH3vv/x9r//8fa///H2wP/w9sD/8PXB//D1wv/v9MT/7vPF/+7zxv/t8sf/7fHI/+zxyf/s8Mr/7PDL/+zvzP/s78z/7O/M/+zuzP/s7sz/7O7M/+zuzP/t7sz/7e7L/+7uy//u78r/7u/J/+/vyf/v78j/7+/I/+/vyP/w78j/AIEAfv8A8fa///H2v//x9sD/8fXA//D1wf/w9ML/7/TD/+/zxP/u88b/7vLH/+3xyP/t8cn/7PDK/+zvy//s78z/6+7N/+vuzf/r7s7/6+3O/+vtzv/s7c7/7O3N/+ztzf/t7c3/7e3M/+7tzP/u7cv/7u3L/+/uyv/v7sr/7+7K/+/uyv8AgQB+/wDy9cD/8fXA//H1wP/x9cH/8fTC//D0w//w88T/7/PF/+7yxv/u8cf/7fDJ/+3wyv/s78v/7O7M/+zuzf/r7c7/6+3O/+vtz//r7M//6+zP/+zsz//s7M//7OzO/+3szv/t7M7/7uzN/+7szf/u7Mz/7+zM/+/sy//v7Mv/7+zL/wCBAH7/APL1wP/y9cD/8fTB//H0wf/x9ML/8PPD//DzxP/v8sX/7/HH/+7wyP/t8Mn/7e/L/+zuzP/s7s3/7O3O/+ztzv/r7M//6+zP/+vr0P/s69D/7OvQ/+zr0P/s68//7evP/+3rz//u687/7uvO/+7rzf/v683/7+vN/+/rzP/v68z/AYEAfv8A8vTA//L0wP/y9MH/8fTB//Hzwv/w88P/8PLE/+/xxv/v8cf/7vDI/+7vyv/t78v/7e7M/+ztzf/s7c7/7OzP/+zsz//r69D/7OvQ/+zr0P/s6tD/7OrQ/+3q0P/t6s//7erP/+7qz//u6s7/7urO/+/qzf/v683/7+vN/+/rzf9kmGHjAHUKXgAAAABJRU5ErkJggg==)
*Add caption explaining what this shows*

![Screenshot2]([Add screenshot 2 here with proper name](https://media.discordapp.net/attachments/990517020762193951/1401243926446346340/reply.PNG?ex=688f9199&is=688e4019&hm=c02deab9f4172b5472b050aa4c83a1608789dd0e61d3b5eac38ab8a64182b5ac&=&format=webp&quality=lossless))
*Add caption explaining what this shows*

![Screenshot3]([Add screenshot 3 here with proper name](https://media.discordapp.net/attachments/990517020762193951/1401243927075622964/listening.PNG?ex=688f919a&is=688e401a&hm=b288a000fa9111e1d10fd0e92852113aef91c1be4cb71986755183699367b971&=&format=webp&quality=lossless))
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


