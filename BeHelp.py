from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import re
import os,pathlib
import sys
from subprocess import Popen
import traceback
from os import path, walk
import sqlite3
#import pandas as pd
from shutil import copyfile # copy2, copytree, rmtree,
# from distutils.dir_util import remove_tree , copy_tree 有 BUG

g_allRegexs = None
g_esProjPath = ""
g_reportLogs = None
g_isOverWriteSource = False #是否複寫原始碼


class QtUIHelp(object):
    @staticmethod
    def toCenter(ui:QtWidgets.QMainWindow):
        qr = ui.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        ui.move(qr.topLeft())

    @staticmethod
    def doFixedSize(ui:QtWidgets.QMainWindow):
        ui.setFixedSize(ui.frameGeometry().width(),ui.frameGeometry().height())

class OSHelp(object):
    @classmethod
    def verCanRun(cls):
        verNum = 10000*(sys.version_info[0]) + 100 * (sys.version_info[1]) + sys.version_info[2]
        if(verNum < 30600):
            return False,"3.6"
        return True,"3.6"

    @classmethod
    def bundlePath(cls):
        return path.dirname(path.abspath(__file__))

    @classmethod
    def launchPath(cls):
        '''
        起始目錄
        '''
        if(sys.platform == "darwin"):
            dirPath = path.dirname(path.dirname(path.dirname(path.dirname(sys.argv[0]))))
        else:
            dirPath = path.dirname(sys.argv[0])
        if(sys.argv[0] == ""):
            dirPath = path.dirname(path.abspath(__file__)) #pyinstaller
        dirPath = path.abspath(path.curdir)
        return dirPath
    
    @staticmethod
    def genPathList(rootPath:str, includeDir:bool = False, extList:list = None, lst:list = None) ->list:
        '''產生檔案與目錄集
        ---
        rootPath: 根目錄
        includeDir: 輸出是否包含目錄
        extList: 副檔名 List, 如 ['.JPEG','.CR2'],  ['*'] 為全部
        lst: <class 'nt.DirEntry'> 物件的 List 集合
        '''
        if extList == None:
            extList = ["*"]
        if lst == None:
            lst = []
        try:
            for f in os.scandir(rootPath):
                #print(type(f))
                if f.is_dir():
                    if includeDir:
                        lst.append(f)
                    OSHelp.genPathList(f.path,includeDir,extList,lst)
                elif f.is_file():
                    if pathlib.Path(f.path).suffix.upper() in extList or extList == ['*']:
                        lst.append(f)
        except Exception as e:
            print("\"{}\" {}:{}".format(rootPath, type(e),str(e)))
        return lst

    @classmethod
    def LocalizeFilesPath(cls):
        '''
        程式的資源目錄的目錄
        '''
        return path.join(OSHelp.bundlePath(), "LocalizeFiles")

    @classmethod
    def outputPath(cls):
        '''
        程式結果輸出目錄
        '''
        global g_esProjPath
        if(g_esProjPath == ""):
            g_esProjPath = OSHelp.launchPath()
        if(g_isOverWriteSource):
            _outputPath = g_esProjPath #輸出到 EmulationStation 目錄
        else:
            _outputPath = path.join(path.dirname(g_esProjPath),"output") #輸出到 Output 目錄
        return _outputPath

    @classmethod
    def reportFile(cls):
        '''
        報告檔案路徑
        '''
        return path.join(OSHelp.outputPath(), "reports.txt")
    
    @staticmethod
    def newConsole():
        if sys.platform == "win32":
            p1 = Popen('start', shell=True)
        elif sys.platform == "linux":
            p1 = Popen('gnome-terminal', shell=True)



class DBHelp(object):
    @staticmethod
    def dict_factory(cursor, row):
        d:dict = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    @classmethod
    def allRegexs(cls, _tbName:str = "es_regex"):
        dbFileName = "regexlist.db"
        dbPath = path.join(OSHelp.bundlePath(),dbFileName)
        if (not path.exists(dbPath)):
            return None, "Regex DATA file [{}] does not exists !".format(dbFileName)
        l_sql = "SELECT ord, pattern, repl, ext, comment, active FROM {tbname} ORDER BY ord ; ".format(tbname=_tbName)
        conn = sqlite3.connect(dbPath)
        conn.row_factory = DBHelp.dict_factory
        rows = conn.execute(l_sql).fetchall()
        conn.close()
        return rows,""

    '''
    @classmethod
    def allSettings_old(cls, _tbname:str = "es_regex"):
        _dbfilename = "regexlist.db";
        if (not path.exists(path.join(OSHelp.bundlePath(),_dbfilename))):
            return None, "Regex DATA file [{}] does not exists !".format(_dbfilename)
        conn = sqlite3.connect("regexlist.db")
        l_str = "SELECT ord, pattern, repl, ext, comment FROM {tbname} ORDER BY ord ; ".format(tbname=_tbname)
        resc = pd.read_sql(l_str, conn)
        conn.close()
        #print(allregs.to_dict(orient='records'))
        return resc.to_dict(orient='records') , ""
    '''

class RegExHelp(object):
    @classmethod
    def copyLocalizeFiles(cls):
        _bundlePath = OSHelp.LocalizeFilesPath()
        _localizefiles = []
        _localizeDirs = []
        for root, dirs, files in walk(_bundlePath):
            for d in dirs:
                if(root.count(".") <=0 and d[:1] != "."):
                    fullpath = path.join(root, d)
                    _localizeDirs.append(fullpath)
        for root, dirs, files in walk(_bundlePath):
            for f in files:
                if(root.count(".") <=0 and f[:1] != "."):
                    fullpath = path.join(root, f)
                    _localizefiles.append(fullpath)
        
        _outputPath = OSHelp.outputPath()
        _successful = True
        _errorString = ""
        try:
            for d in _localizeDirs:
                dstDir = d.replace(_bundlePath,_outputPath)
                os.makedirs(dstDir,exist_ok=True)
        
            for f in _localizefiles:
                dstFile = f.replace(_bundlePath,_outputPath)
                if os.path.exists(dstFile):
                    os.remove(dstFile)
                copyfile(path.join(_bundlePath,f),dstFile)
        except Exception as e:
            print("Error: type= {}".format(str(type(e))))
            print(e.args)
            print(e)
            _successful = False
            _errorString = str(e)
        return _successful, _errorString

    @classmethod
    def Prepare(cls, p_espath, p_owsrc:bool = False, p_tablebName:str = "es_regex"):
        '''
        開始正則處理時預先動作
        ---
        p_espath : 選擇的專案目錄
        p_owsrc  : 選擇是否覆蓋原始碼
        p_tablebName : 資料表名稱
        
        '''
        global g_allRegexs ,g_esProjPath, g_reportLogs, g_isOverWriteSource
        # 參數設定與檢查
        if(p_espath == "" or p_espath == None):
             return False, "No ES project path assign."
        g_isOverWriteSource = p_owsrc
        g_esProjPath = p_espath

        _success, _errStr = RegExHelp.copyLocalizeFiles()
        if( not _success):
            return _success, _errStr
        if(g_allRegexs == None):
            g_allRegexs , _errStr = DBHelp.allRegexs(p_tablebName)
        if( not g_allRegexs and _errStr != ""):
            return _success, _errStr

        if(g_reportLogs == None):
            g_reportLogs = []
        else:
            g_reportLogs.clear()     
        return True,""

    @classmethod
    def doSub(cls, filePath:str, rootPath:str, tbName:str = "es_regex"):
        '''
        正規取代
        ---
        filePath : 原始檔案路徑
        rootPath : 專案路徑
        '''
        global g_allRegexs
        filename = os.path.basename(filePath)
        errorString = None
        if(g_allRegexs == None):
            g_allRegexs, errorString = DBHelp.allRegexs(tbName)
        try:
            f = open(filePath,'r',encoding="utf-8")
            sourceCode = f.read()
            f.close()
        except UnicodeDecodeError:
            print("UnicodeDecodeError Error: {}".format(filePath))
            return
        except Exception as e:
            print("Error({}) {}".format(str(e),filePath))
            return
        except BaseException as e:
            print(filePath)
            print(repr(e))
            print(str(traceback.format_exc()))
            return
        except:
            print("Other open error")
            return
        isMatch = False
        for reg in g_allRegexs:
            if(reg["active"] != "Y"):
                continue
            ext = "({})".format(reg["ext"].replace("*.",".*."))
            matchFile = re.findall(ext,filename,re.I)
            if(not bool(matchFile)):
                #檔案名稱不符正規取代的條件
                continue
            pattern = reg["pattern"]
            matchContent = re.findall(pattern, sourceCode, re.M)
            if(not bool(matchContent)):
                continue
            #print("{}.{}".format(str(type(matchContent)),str(matchContent)))
            RegExHelp.addReport(filePath, reg, matchContent)
            isMatch = True
            repl = reg["repl"].replace("$1","\\1").replace("$2","\\2").replace("$3","\\3").replace("$4","\\4").replace("$5","\\5").replace("$6","\\6").replace("$7","\\7").replace("$8","\\8")
            sourceCode = re.sub(pattern,repl, sourceCode)
        if(isMatch): #符合並已經正規取代
            refDirName = path.dirname(filePath).replace(rootPath,"")
            if(refDirName[:1] == "/" or refDirName[:1] == "\\"):
                refDirName = refDirName[1:]
            newPath = path.join(OSHelp.outputPath(),refDirName)
            if( not path.exists(newPath)):
                os.makedirs(newPath)
            newFilePath = path.join(newPath,filename)
            f = open(newFilePath,'w')
            f.write(str(sourceCode))
            f.close

    @classmethod
    def addReport(cls, filePath:str, regItem:dict, match:list):
        '''
        新增 Log 資訊
        '''
        global g_reportLogs
        if ( not bool(match)):
            return
        if(g_reportLogs == None):
            g_reportLogs = []
        d:dict = {"ord" : regItem["ord"], "repl" : regItem["repl"], "pattern" : regItem["pattern"], "comment" : regItem["comment"], "filename" : filePath, "match" : len(match)}
        g_reportLogs.append(d)
        return

    @classmethod
    def writeReport(cls):
        global g_reportLogs
        g_reportLogs.sort(key = lambda s: s["filename"])
        try:
            f = open(OSHelp.reportFile(),'a+', encoding='utf-8')
            totalMatchCount = 0
            for log in g_reportLogs:
                totalMatchCount = totalMatchCount + int(log["match"])
                oFileName = path.basename(log["filename"])
                ofPath = path.dirname(log["filename"].replace(g_esProjPath,""))[1:]
                logtext = "{_ord} {_filenm}(found={_match})\t{_fPath}\n".format(_ord=log["ord"], _filenm =oFileName, _fPath =ofPath,  _match = log["match"])
                f.write(logtext)
            f.write('\nTotal found : {}\n\n'.format(totalMatchCount))
            f.close()
        except Exception as e:
            print("writeReport Error: type= {}".format(str(type(e))))
            print(e.args)
            print(e)
        except:
            print("writeReport Other open error")