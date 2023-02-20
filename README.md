[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



# LocalDB

**localDB** is a Python package that allows you to generate a local database in the file system. With **localDB**, users can *create, update, delete*, and *search* a local database on their system. This package can be useful for applications that reire a simple and efficient local data storage solution. Additionally, being a local database solution, it does not require an internet connection or depend on external services.


## FolderData

- createData(self, name: str) -> object:
   This method creates a new directory with the given name. It first checks whether a directory with the same name already exists or not. If it exists, then it raises an error message and returns None. Otherwise, it creates the new directory and returns the directory object. A message is printed to confirm that the directory has been created.

- removeData(self, name: str) -> object:
   This method removes the directory with the given name. It first checks whether the directory exists or not. If it doesn't exist, it raises an error message and returns None. Otherwise, it removes the directory and returns the directory object.

- findData(self, name: str) -> bool:
  This method checks whether a directory with the given name exists or not. It returns a boolean value of True if the directory exists, and False if it doesn't exist.

## Chases

- The `createChase` method takes two arguments, name and chase. It checks if a data folder with the given name exists using the findData method. If it does not exist, it raises a TypeError. Otherwise, it creates a new text file with the given name in the data folder and returns the file object.
Example:
```localdb.createChase("dataName", "chaseName")```

- The  `setChase` method takes four arguments, name, chase, __newContent, and edit. It checks if the edit argument is either "a" or "w". If it is not, it raises a TypeError. It also checks if the data folder with the given name exists. If it does not exist, it raises a TypeError. Then, it opens the text file with the given name in the data folder with the appropriate editing mode. It writes the new content to the file and returns the number of characters written.
Example:
```localdb.createChase("dataName", "chaseName", "content", "editType")```


These methods can be useful for managing and updating text files within a local data folder in a Python application.
## Authors

- [@thiagostilo2121](https://www.github.com/thiagostilo2121)
