import speech_recognition as sr
from pydub import AudioSegment

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone()

with mic as source:
    print("Bir sey soyleyin\n")
    recognizer.adjust_for_ambient_noise(source)
    print("Kayit icin hazir\n")
    audio = recognizer.listen(source)
    print("Ses Kaydedildi\n")
    try:
        text = recognizer.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Soylediginizi tam anlayamadim.\n")
    except sr.RequestError:
        print("Ses algilama servisi coktu\n")