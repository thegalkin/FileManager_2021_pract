'''
Документация

Создание папки - createDir имя_папки

Удаление папки - removeDir имя_папки

Создание файла - createFile имя_файла

Запись в файл - writeToFile имя_файла

Чтение файла - readFile имя_файла

Удаление файла - deleteFile имя_файла

Копирование вставка - copyPaste имя_файла_исходного имя_папки

Вырезание вставка cutPaste имя_файла_исходного имя_папки

Переименование файла renameFile имя_файла

'''


from os import chdir, mkdir, pathconf, path, remove, rename, rmdir
import shutil as sh


class FileManager:
    chosenFolderName = ""
    pathToFolder = path(chosenFolderName)

    def __init__(self, folder):
        with open("settings.txt", "r") as f:
            self.chosenFolder = f.read()
        self.eraseToBaseFolder()

    def eraseToBaseFolder(self):
        chdir(self.pathToFolder)
    
    def 

    def createDir(self, name):
        mkdir(name)

    def deleteDir(self, name):
        rmdir(name)
    
    def changeDir(self, name):
        chdir(name)
    
    def createFile(self, name):
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
    
    def cutPaste(self, name, whereTo):
        sh.move(name, path.join(self.pathToFolder, whereTo))
    
    def renameFile(self, oldName, newName):
        rename(oldName, newName)
    
def cmdCheck(inp, cmdName):
    if imp == cmdCheck:
        return True
    else:
        return False


cmds = []
fm = FileManager()
while cmds[0] != "exit":
    cmds = input().split(" ")
    cmd = cmd[0]
    cmdBody = cmd[1] #если команда короткая
    if cmdCheck(cmd, "createDir"):
        fm.createDir(cmdBody)
    if cmdCheck(cmd, "deleteDir"):
        fm.deleteDir(cmdBody)
    if cmdCheck(cmd, "createFile"):
        fm.createFile(cmdBody)
    if cmdCheck(cmd, "writeToFile"):
        fm.writeToFile(cmds[1], cmds[2])
    if cmdCheck(cmd, "readFile"):
        fm.readFile(cmdBody)
    if cmdCheck(cmd, "deleteFile"):
        fm.deleteDir(cmdBody)
    if cmdCheck(cmd, "copyPaste"):
        fm.copyPaste(cmds[1], cmds[2])
    if cmdCheck(cmd, "cutPaste"):
        fm.cutPaste(cmds[1], cmds[2])
    if cmdCheck(cmd, "renameFile"):
        fm.renameFile(cmds[1], cmds[2])

