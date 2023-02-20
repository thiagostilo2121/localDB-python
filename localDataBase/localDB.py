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

Information
-----------
Version: 0.0.9
Developer: Thiago Stilo
GitHub: github.com/thiagostilo2121

"""

__all__= [
    "createData",
    "removeData",
    "findData",
    "createChase",
    "setChase",
]

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
             raise TypeError("The folder dosen't exists")
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
             raise TypeError("The DataFolder dosen't exists")
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
             raise TypeError("The DataFolder dosen't exists")
             return
         with open(f"{name}/{chase}.txt", edit) as local:
             rt = local.write(__newContent)
             return rt

                          
         
_inst = folderData()
createData = _inst.createData
removeData = _inst.removeData
findData = _inst.findData
_chst = chases()
createChase = _chst.createChase
setChase = _chst.setChase