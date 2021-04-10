import os
import pathlib
import shutil
import json

try:
    with open(f"{os.path.abspath(os.getcwd())}/settings.json") as settings:
        settings = json.load(settings)
except FileNotFoundError:
    print("Settings file (settings.json) does not exist.")
    print("See README: https://github.com/onyxcode/pish#instructions")
    lin_home = " "
else:
    lin_home = settings['HOMEDIR']




class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

while True:
    try:
        stdin = input(f"{Color.BOLD}{os.path.abspath(os.getcwd()).replace(lin_home, '~')}{Color.END}\n(> ")
        if stdin == "exit":
            exit()
        if stdin == "clear":
            os.system('clear')
        if stdin == "help":
            print(f"""{Color.BOLD}Commands:{Color.END}
    clear       Clears screen.
    exit        Exits shell.
    help        Shows this message.
    mkd         Creates new directory.
    rm          Removes file.
    rmd         Removes directory.""")
        if stdin.startswith("mkd"):
            newdir = stdin.split(" ")[1]
            if os.path.exists(newdir):
                print("Directory already exists.")
            else:
                os.mkdir(newdir)
        if stdin.startswith("rm "):
            targfile = stdin.split(" ")[1]
            if os.path.exists(targfile):
                if os.path.isdir(targfile):
                    print("Please use rmd for directories.")
                else:
                    os.remove(targfile)
            else:
                print("File does not exist.")
        if stdin.startswith("rmd "):
            targdir = stdin.split(" ")[1]
            if os.path.exists(targdir):
                if os.path.isfile(targdir):
                    print("Please use rm for files.")
                else:
                    shutil.rmtree(targdir)
            else:
                print("Directory does not exist.")

    except EOFError:
        print("")
        exit()
    except KeyboardInterrupt:
        print("")
        exit()
    else:
        pass