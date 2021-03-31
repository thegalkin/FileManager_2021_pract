

from os import chdir, getcwd, mkdir, pathconf, path, remove, rename, rmdir, walk
from posix import listdir
import shutil as sh


class FileManager:
    motherPath = ""
    

    def __init__(self):
        with open("settings.txt", "r") as f:
            self.motherPath = f.read()
        self.eraseToBaseFolder()

    def eraseToBaseFolder(self):
        chdir(self.motherPath)

    
    def moveUp(self):
        chdir(self.motherPath.parent)
        print("\n moving up \n")

    def openDir(self, name):
        chdir(path.join(getcwd(), name))
        print("\n opening dir...\n")

    def createDir(self, name):
        mkdir(name)
        print("\ncreating dir\n")

    def deleteDir(self, name):
        rmdir(name)
        print("\ndeleting dir\n")
    
    def changeDir(self, name):
        chdir(name)
        print("\nchanging dir\n")
    
    def createFile(self, name):
        f = open(name, "w+")
        f.write("")
        f.close()
        print("\ncreating file\n")
    
    def writeToFile(self, name, text):
        with open(name, "a") as f:
            f.write(text)
        print("\nwriting to file\n")
    
    def readFile(self, name):
        with open(name, "r") as f:
            print(f.read())
        print("\nreading file\n")
    
    def deleteFile(self, name):
        remove(name)
        print("\ndeleting file\n ")
    
    def copyPaste(self, name, whereTo):
        if whereTo == "..":
            sh.copyfile(name, path.join(self.motherPath, name))
        else:
            sh.copyfile(name, path.join(self.motherPath, whereTo))
        print("\ncopying\n ")

    def cutPaste(self, name, whereTo):
        if whereTo == "..":
            sh.move(name, path.join(self.motherPath, name))
        else:
            sh.move(name, path.join(self.motherPath, whereTo))
        print("\ncutting\n ")

    def renameFile(self, oldName, newName):
        rename(oldName, newName)
        print("\nrenaming\n")
    
    def ls(self):
        list(map(print,listdir()))

def cmdCheck(inp, cmdName):
    if inp == cmdName:
        return True
    else:
        return False


cmds = ["",]
fm = FileManager()
while cmds[0] != "exit":
    cmds = input().split(" ")
    if len(cmds) > 0 and cmds[0] != "":
        cmd = cmds[0]
    else:
        print("empty line \n")
        pass
    if len(cmds) > 1:
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
        fm.deleteFile(cmdBody)
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
    if cmdCheck(cmd, "ls"):
        fm.ls()
    cmds = [""]