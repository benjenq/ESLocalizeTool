# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/psf/RamDisk/ESLocalizeTool/DlgSuccess.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 228)
        Dialog.setMinimumSize(QtCore.QSize(346, 228))
        Dialog.setMaximumSize(QtCore.QSize(346, 228))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/resources/icon_yes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(False)
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(93, 177, 163, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnClose.setFont(font)
        self.btnClose.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/png/resources/es_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setIconSize(QtCore.QSize(26, 22))
        self.btnClose.setObjectName("btnClose")
        self.lb_msgtitle = QtWidgets.QLabel(Dialog)
        self.lb_msgtitle.setGeometry(QtCore.QRect(87, 12, 235, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_msgtitle.setFont(font)
        self.lb_msgtitle.setObjectName("lb_msgtitle")
        self.lb_icon = QtWidgets.QLabel(Dialog)
        self.lb_icon.setGeometry(QtCore.QRect(39, 12, 40, 40))
        self.lb_icon.setStyleSheet("image: url(:/png/resources/icon_yes.png);")
        self.lb_icon.setText("")
        self.lb_icon.setObjectName("lb_icon")
        self.tb_script_linux = QtWidgets.QPlainTextEdit(Dialog)
        self.tb_script_linux.setGeometry(QtCore.QRect(9, 125, 247, 40))
        self.tb_script_linux.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_script_linux.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_script_linux.setReadOnly(True)
        self.tb_script_linux.setPlainText("")
        self.tb_script_linux.setObjectName("tb_script_linux")
        self.btnCopy = QtWidgets.QPushButton(Dialog)
        self.btnCopy.setGeometry(QtCore.QRect(267, 126, 67, 37))
        self.btnCopy.setStyleSheet("background-color: rgb(5, 102, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnCopy.setObjectName("btnCopy")
        self.lb_desc = QtWidgets.QLabel(Dialog)
        self.lb_desc.setGeometry(QtCore.QRect(12, 57, 325, 37))
        self.lb_desc.setLineWidth(1)
        self.lb_desc.setWordWrap(True)
        self.lb_desc.setObjectName("lb_desc")
        self.radio_linux = QtWidgets.QRadioButton(Dialog)
        self.radio_linux.setGeometry(QtCore.QRect(12, 95, 79, 23))
        self.radio_linux.setStyleSheet("color: rgb(32, 74, 135);")
        self.radio_linux.setChecked(True)
        self.radio_linux.setObjectName("radio_linux")
        self.radio_rpi = QtWidgets.QRadioButton(Dialog)
        self.radio_rpi.setGeometry(QtCore.QRect(80, 95, 111, 23))
        self.radio_rpi.setStyleSheet("color: rgb(143, 89, 2);")
        self.radio_rpi.setObjectName("radio_rpi")
        self.radio_rpi4 = QtWidgets.QRadioButton(Dialog)
        self.radio_rpi4.setGeometry(QtCore.QRect(195, 95, 136, 23))
        self.radio_rpi4.setStyleSheet("color: rgb(183, 3, 120);")
        self.radio_rpi4.setObjectName("radio_rpi4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Success"))
        self.btnClose.setText(_translate("Dialog", "OK"))
        self.lb_msgtitle.setText(_translate("Dialog", "Localize finished !"))
        self.btnCopy.setText(_translate("Dialog", "Copy"))
        self.lb_desc.setText(_translate("Dialog", "Copy & Paste following script to compile source code."))
        self.radio_linux.setText(_translate("Dialog", "Linux"))
        self.radio_rpi.setText(_translate("Dialog", "Raspberry Pi"))
        self.radio_rpi4.setText(_translate("Dialog", "Raspberry Pi 4B"))
import resource_rc
