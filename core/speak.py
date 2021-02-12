import pyttsx3
from ui import design
from PyQt5 import QtWidgets

engine = pyttsx3.init()

def speak(string, widget):
    engine.say(string)
    engine.runAndWait()
    widget.addItem(string)
    widget.scrollToBottom()
