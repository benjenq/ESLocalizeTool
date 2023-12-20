# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'r:\ESLocalizeTool\UIMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 301)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/resources/es_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 456, 71))
        self.label.setStyleSheet("image: url(:/png/resources/es_logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 85, 506, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(5, 5, 156, 16))
        self.label_2.setObjectName("label_2")
        self.tb_script1 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tb_script1.setGeometry(QtCore.QRect(5, 25, 441, 71))
        self.tb_script1.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.tb_script1.setReadOnly(True)
        self.tb_script1.setObjectName("tb_script1")
        self.tb_script2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.tb_script2.setGeometry(QtCore.QRect(5, 115, 441, 66))
        self.tb_script2.setReadOnly(True)
        self.tb_script2.setObjectName("tb_script2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(5, 95, 181, 16))
        self.label_3.setObjectName("label_3")
        self.btn_cpscript1 = QtWidgets.QPushButton(self.tab_2)
        self.btn_cpscript1.setGeometry(QtCore.QRect(450, 25, 46, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_cpscript1.setFont(font)
        self.btn_cpscript1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cpscript1.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_cpscript1.setObjectName("btn_cpscript1")
        self.btn_cpscript2 = QtWidgets.QPushButton(self.tab_2)
        self.btn_cpscript2.setGeometry(QtCore.QRect(450, 114, 46, 66))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_cpscript2.setFont(font)
        self.btn_cpscript2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cpscript2.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_cpscript2.setObjectName("btn_cpscript2")
        self.btnNewConsole = QtWidgets.QPushButton(self.tab_2)
        self.btnNewConsole.setGeometry(QtCore.QRect(334, 5, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnNewConsole.setFont(font)
        self.btnNewConsole.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNewConsole.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 214, 0);")
        self.btnNewConsole.setObjectName("btnNewConsole")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.chk_owsrc = QtWidgets.QCheckBox(self.tab_1)
        self.chk_owsrc.setGeometry(QtCore.QRect(305, 0, 154, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.chk_owsrc.setFont(font)
        self.chk_owsrc.setStyleSheet("color: rgb(4, 0, 228);")
        self.chk_owsrc.setChecked(True)
        self.chk_owsrc.setObjectName("chk_owsrc")
        self.btnDialogDirectory = QtWidgets.QPushButton(self.tab_1)
        self.btnDialogDirectory.setGeometry(QtCore.QRect(392, 30, 82, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btnDialogDirectory.setFont(font)
        self.btnDialogDirectory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDialogDirectory.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.btnDialogDirectory.setObjectName("btnDialogDirectory")
        self.btnStart = QtWidgets.QPushButton(self.tab_1)
        self.btnStart.setGeometry(QtCore.QRect(10, 75, 466, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.lb_progress = QtWidgets.QLabel(self.tab_1)
        self.lb_progress.setGeometry(QtCore.QRect(10, 140, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lb_progress.setFont(font)
        self.lb_progress.setObjectName("lb_progress")
        self.regexProgress = QtWidgets.QProgressBar(self.tab_1)
        self.regexProgress.setGeometry(QtCore.QRect(75, 140, 400, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.regexProgress.setFont(font)
        self.regexProgress.setProperty("value", 0)
        self.regexProgress.setObjectName("regexProgress")
        self.lb1 = QtWidgets.QLabel(self.tab_1)
        self.lb1.setGeometry(QtCore.QRect(11, 0, 301, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.emuSrcPath = QtWidgets.QLineEdit(self.tab_1)
        self.emuSrcPath.setGeometry(QtCore.QRect(10, 30, 370, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.emuSrcPath.setFont(font)
        self.emuSrcPath.setReadOnly(True)
        self.emuSrcPath.setObjectName("emuSrcPath")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(5, 95, 251, 16))
        self.label_5.setObjectName("label_5")
        self.tb_cpesscript = QtWidgets.QPlainTextEdit(self.tab_3)
        self.tb_cpesscript.setGeometry(QtCore.QRect(5, 115, 441, 66))
        self.tb_cpesscript.setReadOnly(True)
        self.tb_cpesscript.setPlainText("")
        self.tb_cpesscript.setObjectName("tb_cpesscript")
        self.tb_compilescript = QtWidgets.QPlainTextEdit(self.tab_3)
        self.tb_compilescript.setGeometry(QtCore.QRect(5, 25, 441, 71))
        self.tb_compilescript.setReadOnly(False)
        self.tb_compilescript.setPlainText("")
        self.tb_compilescript.setObjectName("tb_compilescript")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(5, 5, 251, 16))
        self.label_6.setObjectName("label_6")
        self.btn_cpesscript = QtWidgets.QPushButton(self.tab_3)
        self.btn_cpesscript.setGeometry(QtCore.QRect(450, 115, 46, 66))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_cpesscript.setFont(font)
        self.btn_cpesscript.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cpesscript.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_cpesscript.setObjectName("btn_cpesscript")
        self.btn_cpcompilescript = QtWidgets.QPushButton(self.tab_3)
        self.btn_cpcompilescript.setGeometry(QtCore.QRect(450, 25, 46, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_cpcompilescript.setFont(font)
        self.btn_cpcompilescript.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cpcompilescript.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_cpcompilescript.setObjectName("btn_cpcompilescript")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emulationstation Locale"))
        self.label_2.setText(_translate("MainWindow", "Dependency packages"))
        self.tb_script1.setPlainText(_translate("MainWindow", "sudo apt install libsdl2-dev libfreeimage-dev libfreetype6-dev libcurl4-openssl-dev rapidjson-dev libasound2-dev libgles2-mesa-dev build-essential cmake fonts-droid-fallback libvlc-dev libvlccore-dev vlc-bin libboost-system-dev libboost-filesystem-dev libboost-date-time-dev libboost-locale-dev libfreeimage-dev libfreetype6-dev libeigen3-dev libcurl4-openssl-dev libasound2-dev git cmake libsdl2-dev gettext -y "))
        self.tb_script2.setPlainText(_translate("MainWindow", "cd ~\n"
"git clone https://github.com/RetroPie/EmulationStation.git\n"
"cd EmulationStation\n"
"git submodule update --init --recursive"))
        self.label_3.setText(_translate("MainWindow", "Download ES source code"))
        self.btn_cpscript1.setText(_translate("MainWindow", "Copy"))
        self.btn_cpscript2.setText(_translate("MainWindow", "Copy"))
        self.btnNewConsole.setText(_translate("MainWindow", "Shell console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Shell script"))
        self.chk_owsrc.setText(_translate("MainWindow", "OverWrite Source ?"))
        self.btnDialogDirectory.setText(_translate("MainWindow", "Choose.."))
        self.btnStart.setText(_translate("MainWindow", "Start localization process"))
        self.lb_progress.setText(_translate("MainWindow", "Progress"))
        self.lb1.setText(_translate("MainWindow", "Source Code (Project) root path :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Localize && compile"))
        self.label_5.setText(_translate("MainWindow", "Copy compiled binary to /opt/ location"))
        self.label_6.setText(_translate("MainWindow", "Compile ES script"))
        self.btn_cpesscript.setText(_translate("MainWindow", "Copy"))
        self.btn_cpcompilescript.setText(_translate("MainWindow", "Copy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Binary install"))
import resource_rc