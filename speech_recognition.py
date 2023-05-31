import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to capture speech input and convert it to text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        # Use the recognizer to convert speech to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, speech recognition service is unavailable.")

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Capture speech input and convert it to text
speech_text = recognize_speech()
print("You said:", speech_text)

# Convert text to speech
speak("You said: " + speech_text)
