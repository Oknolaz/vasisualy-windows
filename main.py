# coding: utf-8

# GUI
from PyQt5 import QtWidgets
from ui import design
from PyQt5 import QtWidgets, QtGui
import sys
from qt_material import apply_stylesheet

# Core
from core import speak
from core import talk
from core import recognise
import random
import speech_recognition

# Skills
from skills import time_date
from skills import exit
from skills import joke
from skills import weather
from skills import music
from skills import open
from skills import screenshot
from skills import search
from skills import poweroff
from skills import ytvideo
from skills import resay
from skills import map
from skills import wiki
from skills import location
from skills import weather_no_city
from skills import translate
from skills import news
from skills import coin
from skills import todolist
from skills import shoplist
from skills import netconnection
from skills import record
from skills import guess_num
from skills import rulette
from skills import math
from skills import crystal_ball


wrong = ("Прости, я тебя не понимаю.", "Мне кажется ты несёшь какой-то бред.", "Что?", "Ты, наверное, ошибаешься. Я тебя не понимаю.", "Извини, я появился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я тебя не понимаю.", "Пожалуйста, не говори слов, которых я незнаю.", "Ты пытаешься оскорбить меня этим?", "Не издевайся надо мной, я знаю не так много слов.", "Извини, я не могу тебя понять.", "А?", "Объясни попроще.", "Пожалуйста, прочитай моё описание. Скорее всего я не умею делать то, что ты меня просишь или попробуй использовать синонимы.", "Ты ошибаешься.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.", "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.") # Ответы на неизвестную команду.

randnum = -1
isGuessNum = False
isRuLette = False

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow, QtWidgets.QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.setFocus()
        speak.speak("Привет, меня зовут Васисуалий. Чем могу быть полезен?", self.listWidget)
        self.lineEdit.editingFinished.connect(self.vasmsg)
        self.pushButton.clicked.connect(self.recogniser)
        
        
    def vasmsg(self):
        # Функция берёт переданный в виджет lineEdit текст, очищает виджет и запускает программу
        self.say = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.scrollToBottom()
        self.say = self.say.capitalize()
        self.program()


    def recogniser(self):
        self.say = recognise.recognise(self, self.listWidget)
        self.program()
        
    def program(self):
        say = self.say
        skillUse = False
        
        if say == '' or say == ' ':
            pass
        else:
            item = QtWidgets.QListWidgetItem(say)
            item.setTextAlignment(0x0002)
            self.listWidget.addItem(item)
            
        if time_date.main(say):
            speak.speak(time_date.main(say), self.listWidget)
            skillUse = True
            
        elif exit.main(say):
            skillUse = True
            
        elif joke.main(say):
            speak.speak(joke.main(say), self.listWidget)
            skillUse = True
            
        elif weather.main(say, self.listWidget):
            skillUse = True
            
        elif music.main(say, self.listWidget):
            skillUse = True
            
        elif open.main(say, self.listWidget):
            skillUse = True
            
        elif screenshot.main(say, self.listWidget):
            skillUse = True
            
        elif search.main(say, self.listWidget):
            skillUse = True
            
        elif poweroff.main(say):
            skillUse = True
            
        elif ytvideo.main(say, self.listWidget):
            skillUse = True
            
        elif resay.main(say, self.listWidget):
            skillUse = True
        
        elif coin.main(say, self.listWidget):
            skillUse = True
            
        elif map.main(say, self.listWidget):
            skillUse = True
            self.dialog = map.OpenVasMap()
            self.dialog.show()
            
        elif wiki.main(say, self.listWidget):
            skillUse = True
            
        elif location.main(say, self.listWidget):
            skillUse = True
        
        elif weather_no_city.main(say, self.listWidget):
            skillUse = True
        
        elif translate.main(say, self.listWidget):
            skillUse = True
            
        elif news.main(say, self.listWidget):
            skillUse = True
        
        elif shoplist.main(say, self.listWidget):
            skillUse = True
            
        elif todolist.main(say, self.listWidget):
            skillUse = True
        
        elif netconnection.main(say, self.listWidget):
            skillUse = True
            
        elif record.main(say, self.listWidget):
            skillUse = True
            
        elif guess_num.isTriggered(say):
            skillUse = True
            global isGuessNum, randnum
            randnum = guess_num.getRandomNum()
            isGuessNum = guess_num.startGame(self.listWidget)
            
        elif rulette.isTriggered(say):
            skillUse = True
            global isRuLette
            isRuLette = rulette.startGame(self.listWidget)
            
        elif math.calculate(say, self.listWidget):
            skillUse = True
            
        elif crystal_ball.main(say, self.listWidget):
            skillUse = True
        
        elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
            speak.tts_d.stop()

        elif isGuessNum:
            isGuessNum = guess_num.game(say, randnum, isGuessNum, self.listWidget)
            
        elif isRuLette:
            isRuLette = rulette.game(say, self.listWidget)
            
        else:
            if talk.talk(say) != "" and not skillUse:
                speak.speak(talk.talk(say), self.listWidget)
            elif not skillUse:
                if say != "":
                    # Фразы для ответа на несуществующие команды
                    randwrong = random.choice(wrong)
                    speak.speak(randwrong, self.listWidget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_red.xml')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
