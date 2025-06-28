import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime, timedelta
import time

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.conversation_log = []
        self.last_activity = datetime.now()
        self.sleeping = False
        self.setup_voice()
        
        self.WEB_URLS = {
            'youtube': 'https://www.youtube.com',
            'whatsapp': 'https://web.whatsapp.com',
            'google': 'https://www.google.com',
            'reddit': 'https://www.reddit.com',
            'instagram': 'https://www.instagram.com',
            'spotify': 'https://open.spotify.com',
            'discord': 'https://discord.com/app',
            'gmail': 'https://mail.google.com'
        }

    def setup_voice(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

    def log_conversation(self, speaker, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {speaker}: {text}"
        self.conversation_log.append(log_entry)
        print(f"\033[94m{log_entry}\033[0m" if speaker == "User" else f"\033[92m{log_entry}\033[0m")

    def update_activity(self):
        self.last_activity = datetime.now()

    def check_sleep(self):
        inactive_time = datetime.now() - self.last_activity
        if inactive_time > timedelta(minutes=1) and not self.sleeping:
            self.sleep()
        return self.sleeping

    def sleep(self):
        self.sleeping = True
        self.speak("I'm going to sleep now. Say 'wake up' when you need me.")
        self.log_conversation("System", "Entered sleep mode")

    def wake_up(self):
        self.sleeping = False
        self.update_activity()
        self.speak("I'm awake now. How can I help you?")
        self.log_conversation("System", "Woke up from sleep mode")

    def speak(self, text, wait=True):
        self.log_conversation("Assistant", text)
        self.engine.say(text)
        if wait:
            self.engine.runAndWait()

    def recognize_speech(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=4)
            command = self.recognizer.recognize_google(audio).lower()
            self.log_conversation("User", command)
            self.update_activity()
            return command
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return ""
        except sr.RequestError:
            self.speak("I'm having trouble with the speech service.")
            return ""
        except Exception as e:
            self.log_conversation("System", f"Recognition error: {str(e)}")
            return ""

    def execute_command(self, command):
        if not command:
            return

        if self.sleeping:
            if "wake up" in command:
                self.wake_up()
            return

        if "wake up" in command:
            self.speak("I'm already awake!")
            return

        for app_name, url in self.WEB_URLS.items():
            if app_name in command:
                self.speak(f"Opening {app_name.capitalize()}")
                webbrowser.open(url)
                return

        if "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
        elif "exit" in command or "quit" in command:
            self.speak("Goodbye! Have a wonderful day.")
            exit()
        else:
            self.speak("I didn't understand that command.")

    def run(self):
        self.speak("Hello! I'm your voice assistant.")
        while True:
            if not self.check_sleep():
                self.log_conversation("System", "Listening...")
                command = self.recognize_speech()
                self.execute_command(command)
            time.sleep(0.5)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
