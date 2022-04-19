# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/psf/RamDisk/ESLocalizeTool/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 302)
        MainWindow.setMinimumSize(QtCore.QSize(500, 302))
        MainWindow.setMaximumSize(QtCore.QSize(500, 302))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/resources/es_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtPath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPath.setGeometry(QtCore.QRect(20, 161, 370, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPath.setFont(font)
        self.txtPath.setReadOnly(True)
        self.txtPath.setObjectName("txtPath")
        self.btnDialogDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.btnDialogDirectory.setGeometry(QtCore.QRect(402, 162, 82, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnDialogDirectory.setFont(font)
        self.btnDialogDirectory.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.btnDialogDirectory.setObjectName("btnDialogDirectory")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(20, 205, 466, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnStart.setFont(font)
        self.btnStart.setStyleSheet("QPushButton{\n"
"background-color: rgb(5, 102, 0);\n"
"alternate-background-color: rgb(85, 87, 83);\n"
"color: rgb(255, 255, 255);}\n"
"QPushButton:disabled{\n"
"background-color: rgb(85, 87, 83);\n"
"}\n"
"")
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QtCore.QSize(28, 23))
        self.btnStart.setObjectName("btnStart")
        self.lb1 = QtWidgets.QLabel(self.centralwidget)
        self.lb1.setGeometry(QtCore.QRect(21, 129, 301, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 27, 471, 81))
        self.label.setStyleSheet("image: url(:/png/resources/es_logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lb_progress = QtWidgets.QLabel(self.centralwidget)
        self.lb_progress.setGeometry(QtCore.QRect(20, 270, 67, 17))
        self.lb_progress.setObjectName("lb_progress")
        self.regexProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.regexProgress.setGeometry(QtCore.QRect(85, 270, 400, 23))
        self.regexProgress.setProperty("value", 0)
        self.regexProgress.setObjectName("regexProgress")
        self.chk_owsrc = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_owsrc.setGeometry(QtCore.QRect(315, 132, 154, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chk_owsrc.setFont(font)
        self.chk_owsrc.setStyleSheet("color: rgb(4, 0, 228);")
        self.chk_owsrc.setChecked(True)
        self.chk_owsrc.setObjectName("chk_owsrc")
        self.label.raise_()
        self.txtPath.raise_()
        self.btnDialogDirectory.raise_()
        self.btnStart.raise_()
        self.lb1.raise_()
        self.lb_progress.raise_()
        self.regexProgress.raise_()
        self.chk_owsrc.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emulationstation Locale"))
        self.btnDialogDirectory.setText(_translate("MainWindow", "Choose.."))
        self.btnStart.setText(_translate("MainWindow", "Start localization process"))
        self.lb1.setText(_translate("MainWindow", "Source Code (Project) root path :"))
        self.lb_progress.setText(_translate("MainWindow", "Progress"))
        self.chk_owsrc.setText(_translate("MainWindow", "OverWrite Source ?"))
import resource_rc
