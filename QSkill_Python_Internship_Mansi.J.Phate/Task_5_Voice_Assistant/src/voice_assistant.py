import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand")
        return ""
    except sr.WaitTimeoutError:
        return ""

# Main Program
try:
    speak("Hello, I am your personal assistant")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello, how can I help you")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {time}")

        elif "your name" in command:
            speak("I am a Python voice assistant")

        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

except KeyboardInterrupt:
    print("\nProgram stopped by user")
    speak("Assistant stopped")
