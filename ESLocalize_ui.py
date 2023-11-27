#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
下載 ES Source Code
git clone --recursive https://github.com/RetroPie/EmulationStation.git
安裝套件
sudo apt install python3-dev python3-pyqt5 qttools5-dev-tools pyqt5-dev-tools
sudo apt install python3-pip
設定 qt for python
pyinstaller 封裝執行檔
pyinstaller --add-data="regexlist.db:." --add-data="LocalizeFiles:LocalizeFiles" -F -w --clean ESLocalize_ui.py
'''
from PyQt5 import QtWidgets #PyQt5 的部分
from PyQt5.QtWidgets import *
from os import walk
from os.path import join
import sys
from RegExHelp import RegExHelp, OSHelp
from math import ceil
import MainWindow, DlgAlert, DlgSuccess #介面

dealFiles = []

class mainWin(QtWidgets.QMainWindow,MainWindow.Ui_MainWindow):
    def __init__(self,parent=None):
        super(mainWin,self).__init__()
        self.setupUi(self)
        self.projRootPath = OSHelp.launchPath()
        self.txtPath.setText(self.projRootPath)
        self.btnDialogDirectory.clicked.connect(self.openDialogDir)
        #https://stackoverflow.com/questions/6784084/how-to-pass-arguments-to-functions-by-the-click-of-button-in-pyqt
        self.btnStart.clicked.connect(lambda: self.doRegexSubProcess(self.btnStart))
        self.center()        
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def chkPyVer(self):
        _canRun, verStr = OSHelp.verCanRun()
        if(not _canRun):
            self.showAlert(1,"Warrning","Notice","Limited functionality.\nPython version was less then {ver}}".format(ver=verStr))

    def openDialogDir(self):
        global dealFiles
        dlg = QFileDialog()
        dlg.setDirectory(self.txtPath.text())
        chooseDirName = dlg.getExistingDirectory(self,"Select Directory")
        #print('type={},val={}'.format(type(chooseDirName),chooseDirName))
        if(chooseDirName != ""):
            dealFiles.clear()
            self.projRootPath = chooseDirName
            self.txtPath.setText(self.projRootPath)
            #https://blog.gtwang.org/programming/python-list-all-files-in-directory/
            for root, dirs, files in walk(self.projRootPath):
                '''for dir in dirs:
                    print("root={},dir={}".format(root,dir))'''
                for f in files:
                    if(root.count(".") <=0 and f[:1] != "."):
                        fullpath = join(root, f)
                        dealFiles.append(fullpath)
            #print(dealfile)
    
    def doRegexSubProcess(self,btn:QPushButton):
        btn.setEnabled(False)
        _canDo , _errStr = RegExHelp.Prepare(p_espath = self.projRootPath, p_owsrc = self.chk_owsrc.isChecked())
        if(not _canDo and _errStr != ""):
            self.showAlert(-1, "Error", "Error!", errStr = _errStr)
            btn.setEnabled(True)
            return
        progress = 0
        totalProg = len(dealFiles)
        for fpath in dealFiles:
            progress = progress + 1
            RegExHelp.doSub(fpath,self.projRootPath)
            self.regexProgress.setValue(ceil(100*float(progress/totalProg)))
            QtWidgets.QApplication.processEvents()
        RegExHelp.writeReport()
        btn.setEnabled(True)
        dlg = DialogSuccess(self,p_projPath = self.projRootPath)
        dlg.exec_()
        dlg.destroy()
    
    def showAlert(self, alertType:int, titleStr:str, msgStr:str, errStr:str = ""):
        '''
        訊息對話框
        ---
        alertType: 類型, 0:Message 1:Warrning -1:Error
        titleStr : 標題
        msgStr   : 訊息
        errStr   : 內容
        
        '''
        dlg = DialogError(self)
        dlg.setWindowTitle(titleStr)
        dlg.lb_Msg.setText(msgStr)
        dlg.lb_err.setText(errStr)
        if alertType == -1:
            dlg.lb_icon.setStyleSheet("image: url(:/png/resources/icon_no.png);")
        elif alertType == 0:
            dlg.lb_icon.setStyleSheet("image: url(:/png/resources/icon_yes.png);")
        elif alertType == 1:
            dlg.lb_icon.setStyleSheet("image: url(:/png/resources/icon_warrning.png);")
        dlg.exec_()
        dlg.destroy()
        pass
        
    def closeEvent(self, evnt):
        pass
        #evnt.ignore()
        #return None

class DialogSuccess(QtWidgets.QDialog, DlgSuccess.Ui_Dialog):
    def __init__(self,parent=None,func=None,p_projPath = ""):
        super(DialogSuccess,self).__init__(parent)
        self.setupUi(self)
        self.projRootPath = p_projPath
        self.btnClose.clicked.connect(self.actClose) #按下確定時
        self.btnCopy.clicked.connect(self.actCopy)
        self.radio_linux.toggled.connect(self.optChanged)
        self.radio_rpi.toggled.connect(self.optChanged)
        self.radio_rpi4.toggled.connect(self.optChanged)
        self.optChanged()

    def optChanged(self):
        cMakeFlag = ""
        if(self.radio_linux.isChecked()):
            cMakeFlag = "-DUSE_OPENGL_21=On"
        elif(self.radio_rpi.isChecked()):
            cMakeFlag = "-DRPI=On"
        elif(self.radio_rpi4.isChecked()):
            cMakeFlag = "-DRPI=On -DUSE_MESA_GLES=On"
        scriptText = "cd {}\nmkdir build\ncd build\ncmake -DFREETYPE_INCLUDE_DIRS=/usr/include/freetype2/ {} ..\nmake -j4\n".format(self.projRootPath,cMakeFlag)
        self.tb_script_linux.setPlainText(scriptText)

    def actCopy(self):
        QApplication.clipboard().setText(self.tb_script_linux.toPlainText())

    def actClose(self):
        self.close()

    def closeEvent(self, evnt):
        pass


class DialogError(QtWidgets.QDialog, DlgAlert.Ui_MsgBox):
    def __init__(self,parent=None,func=None):
        super(DialogError,self).__init__(parent)
        self.setupUi(self)
        self.btnClose.clicked.connect(self.actClose) #按下確定時
        self.func = func
    def actClose(self):
        self.close()

    def closeEvent(self, evnt):
        pass
        #evnt.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = mainWin()
    mainWin.show()
    mainWin.chkPyVer()
    sys.exit(app.exec_())