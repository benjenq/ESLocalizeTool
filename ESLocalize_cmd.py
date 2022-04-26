'''
設定 qt for python
pyinstaller 封裝執行檔
pyinstaller --add-data="regexlist.db:." --add-data="LocalizeFiles:LocalizeFiles" -F --clean ESLocalize_cmd.py
'''

from RegExHelp import *
from os import *
from math import floor
import re

dealFiles = []

class getParaFromInput(object):
    global dealFiles
    def __init__(self) -> None:
        _loop = True
        self.inputSuccess = False
        self.projRootPath = ""
        self.owsc = False
        print("\nThis process need to know something first. Press Ctrl+c to quit anytime.\n")
        while(_loop):
            try:
                if(self.projRootPath == ""):
                    self.projRootPath = input("Please enter EmulationStation Source Path : \n").strip()
                if(re.findall(r"'(.+)'",self.projRootPath,re.M)): # '/xxxx/EmulationStation'
                    self.projRootPath = re.sub(r"'(.+)'","\\1",self.projRootPath,re.M)
                if(not path.exists(self.projRootPath) or self.projRootPath == ""):
                    print('Path is invalid. Please reinput correct path')
                    self.projRootPath = ""
                    continue
                print(f'EmulationStation Source Path is {self.projRootPath}\n')

                in_owsc =  input("Overwrite source code (Yes / No, default is No) : ")
                if(in_owsc.upper() == "Y" or in_owsc.upper() == "YES"):
                    self.owsc = True
                else:
                    self.owsc = False
                if(self.owsc):
                    _owsc = "Yes"
                else:
                    _owsc = "No"
                print(f'You choose overwrite source code is {_owsc}\n')

                in_scriptType =  input("Script type ? 1 - Linux, 2 - Raspbian Pi, 3 - Raspbian Pi 4B  (Default is Linux): ")
                if(in_scriptType == "" or in_scriptType == ""):
                    self.scriptType = "Linux"
                elif(int(in_scriptType) == 2):
                    self.scriptType = "Raspberry"
                elif(int(in_scriptType) == 3):
                    self.scriptType = "Raspberry4b"
                else:
                    self.scriptType = "Linux"
                print(f'You choose script type is {self.scriptType}\n')
                self.inputSuccess = True
                _loop = False
            except KeyboardInterrupt:
                #print ("\nQuit process.")
                self.inputSuccess = False
                _loop = False

if __name__ == '__main__':
    _para = getParaFromInput()
    if(not _para.inputSuccess):
        print("\nProcess Abort\n")
        exit(0)
    for root, dirs, files in walk(_para.projRootPath):
        '''for dir in dirs:
        print("root={},dir={}".format(root,dir))'''
        for f in files:
            if(root.count(".") <=0 and f[:1] != "."):
                fullpath = path.join(root, f)
                dealFiles.append(fullpath)
    _canDo , _errStr = RegExHelp.Prepare(p_espath = _para.projRootPath, p_owsrc = _para.owsc)
    if(not _canDo and _errStr != ""):
        print(f'Error:{_errStr}')
        exit(0)
    _progress = 0
    _totalProg = len(dealFiles)
    for fpath in dealFiles:
        _progress = _progress + 1
        RegExHelp.doSub(fpath,_para.projRootPath)
        print('Process: {}%'.format(floor(100*float(_progress/_totalProg))))
    RegExHelp.writeReport()
    print("ES Localization Process Finished!\n")
    cMakeFlag = ""
    if(_para.scriptType == "Linux"):
        cMakeFlag = "-DUSE_OPENGL_21=On"
    elif(_para.scriptType == "Raspberry"):
        cMakeFlag = "-DRPI=On"
    elif(_para.scriptType == "Raspberry4b"):
        cMakeFlag = "-DRPI=On -DUSE_MESA_GLES=On"
    scriptText = "cd {}\nmkdir build\ncd build\ncmake -DFREETYPE_INCLUDE_DIRS=/usr/include/freetype2/ {} ..\nmake -j4\n".format(_para.projRootPath,cMakeFlag)
    print("Compile ES code command is:\n")
    print(scriptText)