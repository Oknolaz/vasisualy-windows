from ui import settings
from PyQt5 import QtWidgets
import os
from core import defaults


class ShowSettingsWindow(QtWidgets.QWidget, settings.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        appDir = os.path.dirname(os.path.realpath(__file__))
        try:
            os.chdir(f"{appDir}\\..")
            config = open("vasisualy.conf", "r")
            for line in config:
                if "sentences:" in line:
                    sentences = int(line.replace("sentences:", ""))
                elif "music:" in line:
                    musicDir = line.replace("music:", "")

            self.wikiSpin.setValue(sentences)
            self.musicLoc.setText(musicDir)
        except Exception:
            config = defaults.defaults
            self.wikiSpin.setValue(config["sentences"])
            self.musicLoc.setText(config["music"])
        self.musicDir.clicked.connect(self.selectDir)
        self.buttonBox.accepted.connect(self.writeChanges)

    def writeChanges(self):
        appDir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(f"{appDir}\\..")
        config = open("vasisualy.conf", "w")
        config.write(f"sentences:{self.wikiSpin.value()}\n"
                     f"music:{self.musicLoc.text()}")
        config.close()
        self.hide()

    def selectDir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.musicLoc.setText(dir)
