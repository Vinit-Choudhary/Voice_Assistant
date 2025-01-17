# Voice Assistant Project 🎙️✨

This project is a simple yet powerful voice assistant that can interact with users, perform tasks such as Google search, and play music via YouTube—all through voice commands.

## Features 🚀

* **Speech Recognition:** Converts spoken commands into text using Google Speech Recognition.
* **Text-to-Speech (TTS):** Provides spoken responses using pyttsx3.
* **Google Search:** Allows users to search Google by speaking commands.
* **YouTube Music Playback:** Lets users play songs on YouTube by voice command.

## Technologies Used 🛠️

* **Programming Language:** Python
* **Libraries:**
    * speechrecognition: For converting voice to text.
    * pyttsx3: For text-to-speech conversion.
    * googlesearch-python: For performing Google searches via voice commands.
    * webbrowser: For opening YouTube links in the browser.

## How It Works 💡

The voice assistant works in the following steps:

1. **Voice Input:** The assistant listens for your command through the microphone.
2. **Speech Recognition:** The voice input is converted to text and processed.
3. **Action Execution:**
    * **Google Search:** If the command is related to a search, the assistant retrieves and reads out the top Google results.
    * **YouTube Music:** If the command involves playing music, the assistant will open a YouTube search for the song.
    * **Basic Commands:** Responds to greetings, time, and date queries.

## File Structure 📁

* `voice_assistant_main.py`: Core functionality of the voice assistant—handles speech recognition and text-to-speech.
* `google_search_assistant.py`: Adds Google search capability via voice commands.
* `youtube_music_assistant.py`: Plays songs from YouTube based on voice commands.

## Dependencies 📦

Ensure you have the necessary libraries installed:

```bash
pip install SpeechRecognition pyttsx3 googlesearch-python
