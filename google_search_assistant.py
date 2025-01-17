import speech_recognition as sr
import pyttsx3
from googlesearch import search

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define function for speech recognition
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error connecting to Google Speech Recognition.")
        return None

# Define function for text-to-speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to perform a Google search and retrieve results
def google_search(query):
    speak(f"Searching Google for {query}")
    try:
        search_results = search(query, num=5, stop=5, pause=2)
        for i, result in enumerate(search_results, start=1):
            speak(f"Result {i}: {result}")
    except Exception as e:
        print("An error occurred during the search:", e)
        speak("Sorry, I encountered an error while searching. Please try again later.")

# Main loop for interacting with the user
def main():
    speak("Hello! What would you like to search for on Google?")

    while True:
        user_input = listen()

        if user_input:
            if "search for" in user_input:
                query = user_input.replace("search for", "").strip()
                google_search(query)
                break
            elif "exit" in user_input or "quit" in user_input:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()