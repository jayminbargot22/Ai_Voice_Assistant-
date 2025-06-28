# 🗣️ VoiceAssistant-Py

A Python-based voice assistant that recognizes spoken commands and performs actions like opening websites, telling the time or date, and entering sleep mode after inactivity. This project uses speech recognition and text-to-speech capabilities for a smooth and interactive assistant experience.

## 🚀 Features

- 🎤 Voice command recognition
- 💬 Text-to-speech (TTS) responses
- 🌐 Open popular websites via voice (YouTube, Google, WhatsApp, etc.)
- ⏰ Time and date response
- 😴 Auto-sleep mode after 1 minute of inactivity
- 📜 Conversation logging in terminal
- 🛑 Safe shutdown via `"exit"` or `Ctrl+C`

## 📦 Technologies Used

- Python 3.x
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
- [`pyttsx3`](https://pypi.org/project/pyttsx3/)
- [`webbrowser`](https://docs.python.org/3/library/webbrowser.html)
- Built-in modules: `datetime`, `time`, `sys`

## 📁 Project Structure
VoiceAssistant/
├── voice_assistant.py # Main Python script
├── README.md # Project documentation
└── requirements.txt # Required Python packages




## 🤖 VOICE ASSISTANT - INSTALLATION 


Follow the steps below to install and run the Python Voice Assistant on your computer.

----------------------------------
STEP 1: CLONE THE GITHUB REPOSITORY

Open your terminal or command prompt and run:

git clone https://github.com/jayminbaargot22/VoiceAssistant-Py.git
cd VoiceAssistant-Py


----------------------------------
STEP 2: INSTALL PYTHON

Make sure Python 3.8 or later is installed.

Check your Python version with:
python --version

If not installed, download it from:
https://www.python.org/downloads/

----------------------------------
STEP 3: CREATE A VIRTUAL ENVIRONMENT (Optional but Recommended)

Create:
python -m venv venv

Activate it:

For Windows:
venv\Scripts\activate

For Linux/macOS:
source venv/bin/activate

----------------------------------
STEP 4: INSTALL REQUIRED PACKAGES

If you have a requirements.txt file:
pip install -r requirements.txt

Otherwise, install manually:
pip install speechrecognition pyttsx3 pyaudio

NOTE: If 'pyaudio' causes errors on Windows,
download the .whl file from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Then install it with:
pip install path\to\downloaded\pyaudio.whl

----------------------------------
STEP 5: SET UP YOUR MICROPHONE

Make sure your system microphone is enabled and accessible.
This assistant uses your default input device to listen.

----------------------------------
STEP 6: RUN THE ASSISTANT

Start the program with:

python voice_assistant.py

----------------------------------
STEP 7: TRY THESE VOICE COMMANDS

- open youtube
- open whatsapp
- what's the time
- what's today's date
- wake up
- exit

----------------------------------

Need Help?
You can contact the developer via GitHub Issues or Discussions.




## 🚨🚨 REQUIREMENTS - VoiceAssistant 

Below are the required Python packages for running the Voice Assistant:

1. SpeechRecognition
2. pyttsx3
3. pyaudio

---------------------------
To install these packages:
---------------------------

Option 1: Using requirements.txt (if available)
-----------------------------------------------
pip install -r requirements.txt

Option 2: Manual installation
-----------------------------
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio

---------------------------
Important Note for Windows:
---------------------------
If you face issues installing `pyaudio`, download a pre-built .whl (wheel) file from:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Then install it using:
pip install path\to\downloaded\pyaudio.whl

---------------------------
Check installed versions with:
---------------------------
pip freeze


## Advantages & Uses 💡💡

✅ Advantages

[1] Hands-Free Operation
Enables users to perform basic tasks without touching the keyboard or mouse—ideal for multitasking or accessibility.

[2] Time-Saving
Quick execution of voice commands like opening websites or checking time/date without manual input.

[3]cCustomizable and Extendable
Built with Python, making it easy for developers to modify, add new commands, or integrate with other apps.

[4] Auto Sleep Function
Smart inactivity detection ensures that the assistant isn’t consuming resources when not in use.

[5] Lightweight
Doesn’t require heavy frameworks or APIs. It runs smoothly on most systems with basic Python support.

[6] Offline Speech Capability
The TTS (Text-to-Speech) part works offline, ensuring partial functionality without internet.

[7] Clear Voice Feedback
Responds with natural-sounding voice output, enhancing the interactivity.

[8] Cross-Platform Compatibility
Runs on Windows, macOS, and Linux with minor adjustments.


🛠️ Uses

[1] Personal Productivity
Open frequently used websites like Gmail, YouTube, or Google Search using voice commands.

[2] Accessibility Aid
Helps users with limited mobility interact with their system using voice.

[3] Learning & Teaching Tool
Excellent beginner project to understand Python, speech recognition, TTS, and user interaction.

[4] Voice-Controlled Browsing
Automates repetitive tasks like opening web apps or services.

[5] Voice-Enabled Prototypes
Serve as a base for building advanced virtual assistants, AI agents, or smart desktop interfaces.

[6] Home Automation (with extensions)
Can be integrated with smart home platforms to control devices through speech.


