import pyttsx3
from pygame import mixer
import os
import time

def speak(name: str):
    mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1.0)
    textToSpeak = f'Hurray {name} ,won!'

    audio_dir = 'mains/Saved_Audio'
    audio_path = f'{audio_dir}/{name}.wav'

    os.makedirs(audio_dir, exist_ok=True)

    try:
        if os.path.isfile(audio_path):
            print('Playing from saved audio')
        else:
            print('Generating and saving audio')
            engine.save_to_file(textToSpeak, audio_path)
            engine.runAndWait()

        mixer.music.load(audio_path)
        mixer.music.set_volume(1.0)  # Set volume to max
        mixer.music.play()

        # Wait until the music finishes playing
        while mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"Actual error: {e}")
        raise Exception('Error in speaking')
