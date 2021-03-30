

from os import chdir, getcwd, mkdir, pathconf, path, remove, rename, rmdir
import shutil as sh


class FileManager:
    motherPath = ""
    

    def __init__(self):
        with open("settings.txt", "r") as f:
            self.motherPath = f.read()
        self.eraseToBaseFolder()

    def eraseToBaseFolder(self):
        chdir(self.motherPath)
        print("erasing to base folder")
    
    def moveUp(self):
        chdir(self.motherPath.parent)
        print("moving up")

    def openDir(self, name):
        chdir(path.join(getcwd(), name))
        print("opening dir...")

    def createDir(self, name):
        mkdir(name)
        print("creating dir")

    def deleteDir(self, name):
        rmdir(name)
        print("deleting dir")
    
    def changeDir(self, name):
        chdir(name)
        print("changing dir")
    
    def createFile(self, name):
        f = open(name, "w+")
        f.write("")
        f.close()
        print("creating dir")
    
    def writeToFile(self, name, text):
        with open(name, "a") as f:
            f.write(text)
        print("writing to file")
    
    def readFile(self, name):
        with open(name, "r") as f:
            print(f.read())
        print("reading file")
    
    def deleteFile(self, name):
        remove(name)
        print("deleting file ")
    
    def copyPaste(self, name, whereTo):
        sh.copyfile(name, path.join(self.motherPath, whereTo))
        print("copying ")

    def cutPaste(self, name, whereTo):
        sh.move(name, path.join(self.motherPath, whereTo))
        print("cutting ")
    def renameFile(self, oldName, newName):
        rename(oldName, newName)
        print("renaming")

def cmdCheck(inp, cmdName):
    if inp == cmdName:
        return True
    else:
        return False


cmds = ["", "", ""]
fm = FileManager()
while cmds[0] != "exit":
    cmds = input().split(" ")
    print(cmds)
    cmd = cmds[0]
    cmdBody = cmds[1] 
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
    if cmdCheck(cmd, "moveUp"):
        fm.moveUp()
    if cmdCheck(cmd, "openDir"):
        fm.openDir(cmdBody)
    print("cycle end")