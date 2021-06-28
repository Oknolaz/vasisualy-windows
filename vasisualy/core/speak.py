import pyttsx3
from threading import Thread
from . import defaults

engine = pyttsx3.init()
voices = engine.getProperty("voices")

try:
    voice = defaults.get_value("voice")
    for i in voices:
        if voice == i.name:
            voice = i
except FileNotFoundError:
    voice = None

if voice:
    engine.setProperty("voice", voice.id)


class Speaking(Thread):
    def __init__(self, string):
        Thread.__init__(self)
        self.string = string

    def run(self):
        engine.say(self.string)
        engine.runAndWait()


def speak(string, widget):
    widget.addItem(string)
    widget.scrollToBottom()
    speak_thread = Speaking(string)
    speak_thread.start()
