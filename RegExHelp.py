import re
import os
import sys
from os import path
import sqlite3
#import pandas as pd
from shutil import copytree,rmtree
# from distutils.dir_util import remove_tree , copy_tree 有 BUG

allRegexs = None
esProjPath = ""
reportLogs = None
isOverWriteSource = False #是否複寫原始碼

class OSHelp(object):
    @classmethod
    def verCanRun(cls):
        verNum = 10000*(sys.version_info[0]) + 100 * (sys.version_info[1]) + sys.version_info[2]
        if(verNum < 30800):
            return False
        return True

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
        return dirPath

    @classmethod
    def LocalizeFilesPath(cls):
        '''
        程式的資源目錄的目錄
        '''
        return path.join(OSHelp.bundlePath(), "LocalizeFiles")

    @classmethod
    def outputPath(cls,doCreate:bool = True):
        '''
        程式結果輸出目錄
        '''
        global esProjPath
        if(esProjPath == ""):
            esProjPath = OSHelp.launchPath()
        if(isOverWriteSource):
            outputDirName = esProjPath
            return outputDirName
        outputDirName = path.join(path.dirname(esProjPath),"output")
        if( not path.exists(outputDirName)):
            if(doCreate):
                try:
                    os.makedirs(outputDirName)
                except Exception as inst:
                    print("Error: type= {}".format(str(type(inst))))
                    print(inst.args)
                    print(inst) 
        return outputDirName

    @classmethod
    def reportFile(cls):
        '''
        報告檔案路徑
        '''
        return path.join(OSHelp.outputPath(), "reports.txt")

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
    def Prepare(cls, p_espath, p_owsrc:bool = False, p_tablebName:str = "es_regex"):
        '''
        開始正則處理時預先動作
        ---
        p_espath : 選擇的專案目錄
        p_owsrc  : 選擇是否覆蓋原始碼
        p_tablebName : 資料表名稱
        
        '''
        global allRegexs ,esProjPath, reportLogs, isOverWriteSource
        isOverWriteSource = p_owsrc
        successful = True
        errorString = ""        
        if(p_espath == ""):
            successful = False
            return successful, "No ES project path assign."
        esProjPath = p_espath

        if(reportLogs == None):
            reportLogs = []
        else:
            reportLogs.clear()            

        if(allRegexs == None):
            allRegexs , errorString = DBHelp.allRegexs(p_tablebName)
        if( errorString != ""):
            successful = False
            return successful, errorString

        outputPath = OSHelp.outputPath(False)
        
        if(path.exists(outputPath)):
            if( not isOverWriteSource):
                rmtree(outputPath,ignore_errors = True)
        try:
            if(OSHelp.verCanRun()):
                copytree(src=OSHelp.LocalizeFilesPath(),dst=outputPath,dirs_exist_ok = True)
            else:
                copytree(src=OSHelp.LocalizeFilesPath(),dst=outputPath)
        except Exception as inst:
            print("Error: type= {}".format(str(type(inst))))
            print(inst.args)
            print(inst) 
            successful = False
            errorString = str(inst)
        return successful , errorString


    @classmethod
    def doSub(cls, filePath:str, rootPath:str, tbName:str = "es_regex"):
        '''
        正規取代
        ---
        filePath : 原始檔案路徑
        rootPath : 專案路徑
        '''
        global allRegexs
        filename = os.path.basename(filePath)
        errorString = None
        if(allRegexs == None):
            allRegexs, errorString = DBHelp.allRegexs(tbName)
        try:
            f = open(filePath,'r')
            sourceCode = f.read()
            f.close()
        except UnicodeDecodeError:
            print("UnicodeDecodeError Error: {}".format(filePath))
            return
        except:
            print("Other open error: {}".format(filePath))
            return
        isMatch = False
        for reg in allRegexs:
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
        global reportLogs
        if ( not bool(match)):
            return
        if(reportLogs == None):
            reportLogs = []
        d:dict = {"ord" : regItem["ord"], "repl" : regItem["repl"], "pattern" : regItem["pattern"], "comment" : regItem["comment"], "filename" : filePath, "match" : len(match)}
        reportLogs.append(d)
        return

    @classmethod
    def writeReport(cls):
        reportLogs.sort(key = lambda s: s["filename"])
        try:
            f = open(OSHelp.reportFile(),'a+', encoding='utf-8')
            totalMatchCount = 0
            for log in reportLogs:
                totalMatchCount = totalMatchCount + int(log["match"])
                oFileName = path.basename(log["filename"])
                ofPath = path.dirname(log["filename"].replace(esProjPath,""))[1:]
                logtext = "{_ord} {_filenm}(found={_match})\t{_fPath}\n".format(_ord=log["ord"], _filenm =oFileName, _fPath =ofPath,  _match = log["match"])
                f.write(logtext)
            f.write('\nTotal found : {}\n\n'.format(totalMatchCount))
            f.close()
        except Exception as inst:
            print("writeReport Error: type= {}".format(str(type(inst))))
            print(inst.args)
            print(inst)
        except:
            print("writeReport Other open error")