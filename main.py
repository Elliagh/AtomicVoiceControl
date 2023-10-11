from tkinter import *
from tkinter import ttk
from SpeechRecognize import Recognizer

root = Tk()
root.title("Hackaton")
root.geometry("300x300")

btn = ttk.Button(text="Speak", command=Recognizer.RecognizeVoiceToText)
btn.pack()

root.mainloop()