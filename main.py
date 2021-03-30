'''
Документация

Создание папки - createDir имя_папки

Удаление папки - removeDir имя_папки

Создание файла - createFile имя_файла



'''


from os import chdir, mkdir, pathconf, path, remove, rmdir
import shutil as sh


class FileManager:
    chosenFolderName = ""
    pathToFolder = path(chosenFolderName)

    def __init__(self, folder):
        with open("settings.txt", "r") as f:
            self.chosenFolder = f.read()
    
    def eraseToBaseFolder(self):
        chdir(self.pathToFolder)

    def createDir(self, name):
        mkdir(name)

    def deleteDir(self, name):
        rmdir(name)
    
    def changeDir(self, name):
        chdir(name)
    
    def makeFile(self, name):
        f = open(name, "w+")
        f.write("")
        f.close()
    
    def writeToFile(self, name, text):
        with open(name, "a") as f:
            f.write(text)
    
    def readFile(self, name):
        with open(name, "r") as f:
            print(f.read())
    
    def deleteFile(self, name):
        remove(name)
    
    def copyPaste(self, name, whereTo):
        sh.copyfile(name, path.join(self.pathToFolder, whereTo))
    
    def moveFile