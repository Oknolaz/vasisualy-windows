import pyttsx3

engine = pyttsx3.init()


def speak(string, widget):
    engine.say(string)
    engine.runAndWait()
    widget.addItem(string)
    widget.scrollToBottom()
