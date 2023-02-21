
"""
LocalDB
----

  🟢: Active
  🔴: Deleted
  🟡: Inactive
  ⭕: Comming Soon

  | setData     / 🔴 |

  | readData    / 🔴 |

  | removeData  / 🟢 |

  | createData  / 🟢 |

  | findData    / 🟢 |

  | createChase / 🟢 |

  | setChase    / 🟢 |

  | findChase   / 🟢 |

  | removeChase / 🟢 |

  | readChase  /  🟢 |

Information
-----------
Version: 0.1.3
Developer: Thiago Stilo
GitHub: github.com/thiagostilo2121

"""

__all__= [
    "createData",
    "removeData",
    "findData",
    "createChase",
    "setChase",
    "findChase",
    "removeChase",
    "readChase"
]

dataFolderError_1 = "The DataFolder dosen't exists"

class folderData:

     def __init__(self, x= None) -> None: ...


     def createData(self, name: str) -> object:
         """
         Create a DataFolder and return print("Folder {name} created")
         """
         import os
         path_folder= os.path.exists(f"{name}")

         if path_folder == True:
             raise TypeError("The folder already exist")
             return
         else: 
             _C = os.mkdir(f"{name}")
             print(f"Folder {name} created")
         return _C
             
         
     def removeData(self, name: str) -> object: 
         """
         Remove a DataFolder document
         """
         import os 
         if os.path.exists(f"{name}") == False:
             raise TypeError(dataFolderError_1)
             return
         _D = os.remove(f"{name}")
         return _D
     
     def findData(self, name: str) -> bool:
         """
         Find a DataFolder and return boolean (True or False)
         """

         import os 

         _F = os.path.exists(f"{name}")
         if _F == False:
             _F = False
         elif _F == True:
             _F = True

         return _F        
         
class chases():
     def __init__(self) -> None: ...
     def createChase(self, name: str, chase: str) -> object:
         if findData(f"{name}") == False:
             raise TypeError(dataFolderError_1)
             return
         with open(f"{name}/{chase}.txt", "a") as local:
             local.write("")
         
     def setChase(self, name: str, chase: str, __newContent: str, edit: str) -> object:
         import os
         editd = "a" or "w"

         if edit == editd == False:
             raise TypeError(f"Edit Type: {edit} has not supported! only 'a' or 'w'")
             return
         if findData(name) == False:
             raise TypeError(dataFolderError_1)
             return
         if findData(f"{name}/{chase}.txt") == False:
             raise TypeError("The Chase dosen't exists")
             return
         with open(f"{name}/{chase}.txt", edit) as local:
             rt = local.write(__newContent)
             return rt

     def findChase(self, name: str, chase: str) -> bool:
         import os
         if findData(f"{name}") == False:
             raise TypeError(dataFolderError_1)
             return
         if findData(f"{name}/{chase}.txt") == False:
             _GHd = False
             return _GHd
         elif findData(f"{name}/{chase}.txt") == True:
             _GHd = True
             return _GHd
     def removeChase(self, name: str, chase: str) -> object: 
         if findData(f"{name}") == False:
             raise TypeError(dataFolderError_1)
             return
         if findData(f"{name}/{chase}.txt") == False:
             raise TypeError("The Chase dosen't exists")
             return
         import os 
         os.remove(f"{name}/{chase}.txt")        
     def readChase(self, name: str, chase: str) -> str:
         if findData(f"{name}") == False:
             raise TypeError(dataFolderError_1)
             return
         if findData(f"{name}/{chase}.txt") == False:
             raise TypeError("The Chase dosen't exists")
             return
         import os
         with open(f"{name}/{chase}.txt", "r") as local:
             _READs = local.read()    
             return _READs                      
         
_inst = folderData()
createData = _inst.createData
removeData = _inst.removeData
findData = _inst.findData
_chst = chases()
createChase = _chst.createChase
setChase = _chst.setChase
findChase = _chst.findChase
removeChase = _chst.removeChase
readChase = _chst.readChase