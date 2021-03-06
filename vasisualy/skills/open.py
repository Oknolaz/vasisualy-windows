import webbrowser
from ..core import speak
import subprocess

launch = ("Интернет", "интернет", "Браузер", "браузер", "Сеть", "сеть", "Включи интернет", "включи интернет",
          "Открой браузер", "открой браузер", "Включи браузер", "включи браузер", "Открой интернет", "открой интернет",
          "Включи сеть", "включи сеть", "Включи интернет сеть", "включи интернет сеть", "Всемирная паутина",
          "всемирная паутина", "Открой сеть", "открой сеть", "Подключись", "подключись", "Подключи", "подключи",
          "Подключи меня к сети", "подключи меня к сети", "Подключи сеть", "подключи сеть", "Подключи интернет",
          "подключи интернет", "Открой", "открой", "Запусти", "запусти", "Запуск", "запуск", "Программа", "программа",
          "Приложение", "приложение", "Включи", "включи") # Команды открытия чего-либо

excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися",
               "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий",
               "Пожалуйста", "пожалуйста")


def main(say, widget):
    for i in launch:
        if i in say:

            for net in ("Браузер", "браузер", "Интернет", "интернет", "Сеть", "сеть", "Паутина", "паутина"):
                if net in say:
                    try:
                        # Открытие браузера
                        webbrowser.open_new_tab("https://github.com/Oknolaz/Vasisualy")
                        toSpeak = "Я открыл браузер."
                    except ValueError:
                        toSpeak = "Не удалось открыть веб-браузер"
                            
            for yt in ("Youtube", "youtube", "Ютуб", "ютуб", "Ютьюб", "ютьюб", "Ютюб", "ютюб", "Утуб", "утуб"):
                if yt in say:
                    try:
                        webbrowser.open_new_tab('https://youtube.com/')
                        toSpeak = "Открываю YouTube."
                    except Exception:
                        toSpeak = "Не удалось открыть YouTube."
                            
            for win in ("Окно", "окно", "Окошко", "окошко", "Дверь", "дверь", "Замок", "замок"):
                if win in say:
                    toSpeak = "Очень смешно..."
                    
            for fm in ("Файловый менеджер", "файловый менеджер", "Файлы", "файлы"):
                if fm in say:
                    toSpeak = "Я такого не могу."
                            
            for game in ("Игру", "игру", "Игра", "игра", "Игрушку", "игрушку", "Игрушка", "игрушка", "Майнкрафт",
                         "майнкрафт", "Манкрафт", "манкрафт", "Манкруфт", "манкруфт"):
                if game in say:
                    toSpeak = "Я не могу включать тебе игры. Сам включай!"
                        
            for appStore in ("Центр программ", "центр программ", "аппстор", "апстор", "ап стор", "аппсторе", "апсторе",
                             "ап сторе", "апп стор", "апп сторе", "эппстор", "эппсторе", "эпп стор", "эпп сторе",
                             "эпстор", "эпсторе", "эп стор", "эп сторе", "Центр приложений", "центр приложений",
                             "Магазин программ", "магазин программ", "Магазин приложений", "магазин приложений",
                             "Установщик программ", "установщик программ", "Установщик приложений",
                             "установщик приложений", "Софтвэйр", "софтвэйр", "Софтвар", "софтвар", "Софтваре",
                             "софтваре", "Software", "software"):
                if appStore in say:
                    toSpeak = "Запускаю центр приложений..."
                    try:
                        subprocess.run("gnome-software")
                    except Exception:
                        subprocess.run("plasma-discover")
                    except Exception:
                        toSpeak = "Не удалось запустить центр приложений."
                            
            try:
                app = say.replace(i, '')
                app = app.replace(' ', '')
                for toExclude in excludeList:
                    app = app.replace(toExclude, '')
                subprocess.Popen(app)
                toSpeak = f"Я открыл {app}."
            except Exception:
                pass
            break
        else:
            toSpeak = ""
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
