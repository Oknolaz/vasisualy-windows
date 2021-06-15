import pyttsx3
from threading import Thread

engine = pyttsx3.init()


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