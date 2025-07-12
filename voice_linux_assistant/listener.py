
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"🔊 {text}")
    engine.say(text)
    engine.runAndWait()

def log(text):
    with open("command_log.txt", "a") as f:
        f.write(text + "\n")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say a command:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        speak(f"You said: {command}")
        log(f"[User] {command}")
        return command
    except sr.UnknownValueError:
        speak("I couldn't understand that.")
        log("[Error] Could not understand.")
    except sr.RequestError:
        speak("Network error.")
        log("[Error] Network issue.")
    return ""
