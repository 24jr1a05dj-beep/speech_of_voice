import speech_recognition as sr
from datetime import datetime

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("Please wait, adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Start speaking...")
    audio = recognizer.listen(source)

try:

    text = recognizer.recognize_google(audio)

    print("\nTranscription:")
    print(text)

    # Save transcription to file
    with open("transcription.txt", "a") as file:

        current_time = datetime.now()

        file.write(
            f"\n[{current_time}]\n"
        )

        file.write(text + "\n")

    print("\nTranscription saved successfully!")

except sr.UnknownValueError:

    print("Sorry, I could not understand the audio.")

except sr.RequestError:

    print("Speech recognition service is unavailable.")
