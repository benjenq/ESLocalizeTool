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
from PyQt5 import QtWidgets,QtCore #PyQt5 的部分
from PyQt5.QtWidgets import *
#from os import walk
#from os.path import join
import sys
from BeHelp import *
from math import ceil
import UIMainWindow, UIDlgAlert, UIDlgSuccess #介面

class mainWin(QtWidgets.QMainWindow,UIMainWindow.Ui_MainWindow):
    def __init__(self,parent=None):
        super(mainWin,self).__init__()
        self.setupUi(self)
        self.emuSrcPath.setText(OSHelp.launchPath())
        self.genCpESScript(OSHelp.launchPath())
        self.btnDialogDirectory.clicked.connect(self.openDialogDir)
        #https://stackoverflow.com/questions/6784084/how-to-pass-arguments-to-functions-by-the-click-of-button-in-pyqt
        self.btnStart.clicked.connect(lambda: self.doRegexSubProcess(self.btnStart))
        self.btnNewConsole.clicked.connect(self.newConsole)
        #複製功能
        self.btn_cpscript1.clicked.connect(lambda: self.cpScript(self.btn_cpscript1))
        self.btn_cpscript2.clicked.connect(lambda: self.cpScript(self.btn_cpscript2))
        self.btn_cpcompilescript.clicked.connect(lambda: self.cpScript(self.btn_cpcompilescript))
        self.btn_cpesscript.clicked.connect(lambda: self.cpScript(self.btn_cpesscript))

        QtUIHelp.toCenter(self)
        QtUIHelp.doFixedSize(self)
    
    def chkPyVer(self):
        _canRun, verStr = OSHelp.verCanRun()
        if(not _canRun):
            self.showAlert(1,"Warrning","Notice","Limited functionality.\nPython version was less then {ver}".format(ver=verStr))
        if sys.platform != "linux":
            "For a better experience, please launch on the linux platform"
            self.showAlert(1,"Warrning","Notice","For a better experience,\nplease launch this app on linux platform.")


    def openDialogDir(self):
        global dealFiles
        dlg = QFileDialog()
        dlg.setDirectory(self.emuSrcPath.text())
        chooseDirName = dlg.getExistingDirectory(self,"Select Directory")
        #print('type={},val={}'.format(type(chooseDirName),chooseDirName))
        if(chooseDirName != ""):
            self.emuSrcPath.setText(path.normpath(chooseDirName))
            self.genCpESScript(chooseDirName)
            #https://blog.gtwang.org/programming/python-list-all-files-in-directory/ 停用
            #for root, dirs, files in walk(self.projRootPath):
            '''for dir in dirs:
                    print("root={},dir={}".format(root,dir))'''
                #for f in files:
                    #if(root.count(".") <=0 and f[:1] != "."):
                        #fullpath = join(root, f)
                        #dealFiles.append(fullpath)
            #print(dealfile)
    
    def doRegexSubProcess(self,btn:QPushButton):
        _canDo , _errStr = RegExHelp.Prepare(p_espath = self.emuSrcPath.text(), p_owsrc = self.chk_owsrc.isChecked())
        if(not _canDo and _errStr != ""):
            self.showAlert(-1, "Error", "Error!", errStr = _errStr)
            return
        btn.setEnabled(False)
        dealFiles = OSHelp.genPathList(self.emuSrcPath.text())
        totalProg = len(dealFiles)
        progress = 0
        for f in dealFiles:
            progress = progress + 1
            RegExHelp.doSub(f.path,self.emuSrcPath.text())
            self.regexProgress.setValue(ceil(100*float(progress/totalProg)))
            QtWidgets.QApplication.processEvents()
        RegExHelp.writeReport()
        btn.setEnabled(True)
        dlg = DialogSuccess(self,func=self.callback, p_projPath = self.emuSrcPath.text())
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
    
    def callback(self,compileScript:str):
        self.tb_compilescript.setPlainText(compileScript)
    
    def genCpESScript(self,rootPath:str):
        tmpStr = f"cd {rootPath}\nsudo cp ./emulationstation /opt/retropie/supplementary/emulationstation/\nsudo cp -r locale /opt/retropie/supplementary/emulationstation/"
        self.tb_cpesscript.setPlainText(tmpStr)

    def cpScript(self,btn:QtWidgets.QPushButton):
        if btn == self.btn_cpscript1:
            QApplication.clipboard().setText(self.tb_script1.toPlainText())
        elif btn == self.btn_cpscript2:
            QApplication.clipboard().setText(self.tb_script2.toPlainText())
        elif btn == self.btn_cpcompilescript:
            QApplication.clipboard().setText(self.tb_compilescript.toPlainText())
        elif btn == self.btn_cpesscript:
            QApplication.clipboard().setText(self.tb_cpesscript.toPlainText())
    
    def newConsole(self):
        OSHelp.newConsole()




    def closeEvent(self, evnt):
        pass
        #evnt.ignore()
        #return None

class DialogSuccess(QtWidgets.QDialog, UIDlgSuccess.Ui_Dialog):
    def __init__(self,parent=None,func=None,p_projPath = ""):
        super(DialogSuccess,self).__init__(parent)
        self.setupUi(self)
        self.projRootPath = p_projPath
        self.btnClose.clicked.connect(self.actClose) #按下確定時
        self.btnCopy.clicked.connect(self.actCopy)
        self.chk_rpi.stateChanged.connect(lambda: self.optChanged(self.chk_rpi))
        self.chk_mesa.stateChanged.connect(lambda: self.optChanged(self.chk_mesa))
        self.chk_mesa2.stateChanged.connect(lambda: self.optChanged(self.chk_mesa2))
        self.chk_dispmanx.stateChanged.connect(lambda: self.optChanged(self.chk_dispmanx))
        self.chk_videocore.stateChanged.connect(lambda: self.optChanged(self.chk_videocore))
        self.chk_gles.stateChanged.connect(lambda: self.optChanged(self.chk_gles))
        self.chk_gl.stateChanged.connect(lambda: self.optChanged(self.chk_gl))
        self.cbFunc = func
        
        self.optChanged(None)

    def optChanged(self, chkBox:QtWidgets.QCheckBox):
        cMakeFlag = ""
        if(chkBox != None):
            if(chkBox.objectName() == "chk_mesa"):
                if(chkBox.isChecked() and self.chk_mesa2.isChecked()):
                    self.chk_mesa2.setChecked(False)
            if(chkBox.objectName() == "chk_mesa2"):
                if(chkBox.isChecked() and self.chk_mesa.isChecked()):
                    self.chk_mesa.setChecked(False)
                if(chkBox.isChecked() and self.chk_gl.isChecked()):
                    self.chk_gl.setChecked(False)
            if(chkBox.objectName() == "chk_gl"):
                if(self.chk_mesa2.isChecked()):
                    chkBox.setChecked(False)

        if(self.chk_rpi.isChecked()):
            cMakeFlag += "-DRPI=On "
        if(self.chk_mesa.isChecked()):
            cMakeFlag += "-DUSE_MESA_GLES=On "
        if(self.chk_mesa2.isChecked()):
            cMakeFlag += "-DGL=On -DUSE_GL21=On "
        if(self.chk_dispmanx.isChecked()):
            cMakeFlag += "-DOMX=On "
        if(self.chk_videocore.isChecked()):
            cMakeFlag += "-DUSE_GLES1=On "
        if(self.chk_gles.isChecked()):
            cMakeFlag += "-DGLES=On "
        if(self.chk_gl.isChecked()):
            cMakeFlag += "-DGL=On "
        scriptText = "cd {}\nmkdir build\ncd build\ncmake -DFREETYPE_INCLUDE_DIRS=/usr/include/freetype2/ {}..\nmake -j4 VERBOSE=1\n".format(self.projRootPath,cMakeFlag)
        self.tb_script_linux.setPlainText(scriptText)
        if self.cbFunc != None:
            self.cbFunc(scriptText)

    def actCopy(self):
        QApplication.clipboard().setText(self.tb_script_linux.toPlainText())

    def actClose(self):
        self.close()

    def closeEvent(self, evnt):
        pass


class DialogError(QtWidgets.QDialog, UIDlgAlert.Ui_MsgBox):
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