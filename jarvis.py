import speech_recognition as sr
import webbrowser
import pygame
import threading
import time


# Initialize pygame mixer
pygame.mixer.init()


# Path to your song
SONG_PATH = r"C:\Users\Admin\jarvis\song.mp3.mp3"


activated = False


def play_song():
    try:
        pygame.mixer.music.load(SONG_PATH)
        pygame.mixer.music.play()
        print(" Playing The Clash...")
    except Exception as e:
        print(f"Music error: {e}")


def listen_for_trigger():
    r = sr.Recognizer()


    with sr.Microphone() as source:


        r.adjust_for_ambient_noise(source, duration=1)


        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            return ""


    try:
        command = r.recognize_google(audio).lower()
        print(f"Heard: {command}")
        return command


    except sr.UnknownValueError:
        print("Couldn't understand.")
        return ""


    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return ""


def activate():
    global activated
    if activated:
        return
    activated = True
    print("\n JARVIS ACTIVATED ")
    threading.Thread(target=play_song).start()
    time.sleep(1)
    webbrowser.open("https://www.formula1.com/en/latest/all.html")
    time.sleep(0.5)
    webbrowser.open("https://claude.ai")
    
    # Keep music alive until song ends
    while pygame.mixer.music.get_busy():
        time.sleep(1)


print("JARVIS is running...")


while True:
    command = listen_for_trigger()


    if "daddy" in command:
        activate()

