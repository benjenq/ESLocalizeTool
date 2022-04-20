'''
設定 qt for python
pyinstaller 封裝執行檔
pyinstaller --add-data="regexlist.db:." --add-data="LocalizeFiles:LocalizeFiles" -F --clean ESLocalize_cmd.py
'''

from RegExHelp import *
from os import *
from math import floor

dealFiles = []

class getParaFromInput(object):
    global dealFiles
    def __init__(self) -> None:
        loop = True
        self.inputSuccess = False
        self.projRootPath = ""
        self.owsc = False
        print("\nThis process need to know something first. Press Ctrl+c to quit anytime.\n")
        while(loop):
            try:
                if(self.projRootPath == ""):
                    self.projRootPath = input("Please enter EmulationStation Source Path : \n").strip()
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

                in_scriptType =  input("Script type ? 1 - Linux, 2 - Raspbian OS (Default is Linux): ")
                if(in_scriptType == "" or in_scriptType == ""):
                    self.scriptType = "Linux"
                elif(int(in_scriptType) == 2):
                    self.scriptType = "Raspberry"
                else:
                    self.scriptType = "Linux"
                print(f'You choose script type is {self.scriptType}\n')
                self.inputSuccess = True
                loop = False
            except KeyboardInterrupt:
                #print ("\nQuit process.")
                self.inputSuccess = False
                loop = False

if __name__ == '__main__':
    para = getParaFromInput()
    if(not para.inputSuccess):
        print("Process Abort")
        exit(0)
    for root, dirs, files in walk(para.projRootPath):
        '''for dir in dirs:
        print("root={},dir={}".format(root,dir))'''
        for f in files:
            if(root.count(".") <=0 and f[:1] != "."):
                fullpath = path.join(root, f)
                dealFiles.append(fullpath)
    canDo , errStr = RegExHelp.Prepare(p_espath = para.projRootPath, p_owsrc = para.owsc)
    if(not canDo and errStr != ""):
        print(f'Error:{errStr}')
        exit(0)
    progress = 0
    totalProg = len(dealFiles)
    for fpath in dealFiles:
        progress = progress + 1
        RegExHelp.doSub(fpath,para.projRootPath)
        print('Process: {}%'.format(floor(100*float(progress/totalProg))))
    RegExHelp.writeReport()
    print("ES Localization Process Finished!\n")
    cMakeFlag = ""
    if(para.scriptType == "Linux"):
        cMakeFlag = "-DUSE_OPENGL_21=On"
    elif(para.scriptType == "Raspberry"):
        cMakeFlag = "-DRPI=On -DUSE_MESA_GLES=On"
    scriptText = "cd {}\nmkdir build\ncd build\ncmake -DFREETYPE_INCLUDE_DIRS=/usr/include/freetype2/ {} ..\nmake -j4\n".format(para.projRootPath,cMakeFlag)
    print("Compile ES code command is:\n")
    print(scriptText)