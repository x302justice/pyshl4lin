import os
import sys
def pkg(self):
    print("this is work in progress, so it might be bad")
    if sys.platform == 'win32':
        os.system("pause>nul")
    else:
        input("")
        os.system("clear")
    pkg = input("name of package to install: ")
    dist = input("distro name here")
    if dist == 'ubuntu' or 'mint' or 'debian':
        os.system("sudo apt-get install " + pkg)
    input()
#two lines other than module import and defining.
def pip(self):
    pip = input("name of pip thing here:")
    os.system("pip install " + pip)

def repo(self):
    print("not done yet")
