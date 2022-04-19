# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/psf/RamDisk/ESLocalizeTool/DlgAlert.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MsgBox(object):
    def setupUi(self, MsgBox):
        MsgBox.setObjectName("MsgBox")
        MsgBox.resize(320, 160)
        MsgBox.setMinimumSize(QtCore.QSize(320, 160))
        MsgBox.setMaximumSize(QtCore.QSize(320, 160))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/resources/es_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/png/resources/es_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MsgBox.setWindowIcon(icon)
        self.btnClose = QtWidgets.QPushButton(MsgBox)
        self.btnClose.setGeometry(QtCore.QRect(100, 120, 116, 31))
        self.btnClose.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(243, 243, 243);")
        self.btnClose.setObjectName("btnClose")
        self.lb_Msg = QtWidgets.QLabel(MsgBox)
        self.lb_Msg.setGeometry(QtCore.QRect(141, 30, 141, 36))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_Msg.setFont(font)
        self.lb_Msg.setText("")
        self.lb_Msg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_Msg.setObjectName("lb_Msg")
        self.lb_err = QtWidgets.QLabel(MsgBox)
        self.lb_err.setGeometry(QtCore.QRect(12, 75, 296, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_err.setFont(font)
        self.lb_err.setStyleSheet("color: rgb(204, 0, 0);")
        self.lb_err.setLineWidth(2)
        self.lb_err.setText("")
        self.lb_err.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_err.setWordWrap(True)
        self.lb_err.setObjectName("lb_err")
        self.lb_icon = QtWidgets.QLabel(MsgBox)
        self.lb_icon.setGeometry(QtCore.QRect(80, 25, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_icon.setFont(font)
        self.lb_icon.setStyleSheet("")
        self.lb_icon.setText("")
        self.lb_icon.setObjectName("lb_icon")

        self.retranslateUi(MsgBox)
        QtCore.QMetaObject.connectSlotsByName(MsgBox)

    def retranslateUi(self, MsgBox):
        _translate = QtCore.QCoreApplication.translate
        MsgBox.setWindowTitle(_translate("MsgBox", "Message"))
        self.btnClose.setText(_translate("MsgBox", "OK"))
import resource_rc
