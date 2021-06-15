# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 332)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 616, 268))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wikiLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wikiLabel.setWordWrap(True)
        self.wikiLabel.setObjectName("wikiLabel")
        self.gridLayout_2.addWidget(self.wikiLabel, 3, 0, 1, 1)
        self.wikiSpin = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.wikiSpin.setMinimum(1)
        self.wikiSpin.setMaximum(20)
        self.wikiSpin.setProperty("value", 4)
        self.wikiSpin.setObjectName("wikiSpin")
        self.gridLayout_2.addWidget(self.wikiSpin, 3, 1, 1, 2)
        self.musicLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.musicLabel.setObjectName("musicLabel")
        self.gridLayout_2.addWidget(self.musicLabel, 4, 0, 1, 1)
        self.musicLoc = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.musicLoc.setClearButtonEnabled(False)
        self.musicLoc.setObjectName("musicLoc")
        self.gridLayout_2.addWidget(self.musicLoc, 4, 1, 1, 1)
        self.musicDir = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.musicDir.setObjectName("musicDir")
        self.gridLayout_2.addWidget(self.musicDir, 4, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.wikiLabel.setText(_translate("Dialog", "Количество озвучиваемых предложений из статей на Wikipedia:"))
        self.musicLabel.setText(_translate("Dialog", "Папка с музыкой:"))
        self.musicDir.setText(_translate("Dialog", "..."))