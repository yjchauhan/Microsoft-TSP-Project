import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\notepad.exe",
    'discord': "C:\\Users\\Y. J. Chauhan\\AppData\\Local\\Discord\\app-1.0.9027\\Discord.exe",
}

def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)