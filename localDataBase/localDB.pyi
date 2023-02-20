import localDataBase.localDB as localDB


__all__ = [
     
     "createData",
     "removeData",
     "findData",
     "createChase",
     "setChase",

]



class folderData():
    def __init__(self = None) -> None: ...
    def createData(self, name: str) -> object: ...
    def removeData(self, name: str) -> object: ...
    def findData(self, name: str) -> bool: ...
class chases():
    def createChase(self, name: str, chase: str) -> object: ...    
    def setChase(self, name: str, chase: str, __newContent: str, edit: str) -> object: ...

_inst: folderData = ...
createData = _inst.createData
removeData = _inst.removeData
findData = _inst.findData
_chst: chases = ...
createChase = _chst.createChase
setChase = _chst.setChase
