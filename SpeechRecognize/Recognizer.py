import speech_recognition as sr

class Recognizer:

    def __init__(self):
        self.rec = sr.Recognizer()

    def get_text(self):
        with sr.Microphone() as source:
            print("Скажите что-нибудь...")
            audio = self.rec.listen(source)
        text = self.rec.recognize_google(audio, language="ru-RU")
        return text.lower()


def RecognizeVoiceToText():
    rec = Recognizer()
    try:
        print(rec.get_text())
    except Exception:
        print("something went wrong")
