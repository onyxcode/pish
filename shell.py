import os
import pathlib
import shutil
import json
import glob
import readline
from sys import exit


class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


while True:
    try:
        stdin = input(
            f"{Color.BOLD}{os.path.abspath(os.getcwd()).replace(str(pathlib.Path.home()), '~')}{Color.END}\n➜ "
        )
        readline.write_history_file(f"{os.path.abspath(os.getcwd())}/.pish_history")
        if stdin == "exit":
            print("")
            exit()
        if stdin == "clear":
            print("")
            os.system("clear")
        if stdin == "help":
            print(
                f"""{Color.BOLD}Commands:{Color.END}
    cd          Move to existing directory located elsewhere.
    clear       Clears screen.
    exit        Exits shell.
    help        Shows this message.
    ls          List all files and subdirectories in current directory.
    mkd         Creates new directory.
    rm          Removes file.
    rmd         Removes directory.
    wd          Shows current working directory."""
            )
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
        if stdin.startswith("cd "):
            if stdin.split(" ")[1] == "~":
                if lin_home == " ":
                    print("Home directory is not set.")
                    continue
                else:
                    targdir = settings["HOMEDIR"]
            else:
                targdir = stdin.split(" ")[1]
            if os.path.exists(targdir):
                if os.path.isfile(targdir):
                    print("This is a file, please select a directory.")
                else:
                    os.chdir(targdir)
        if stdin.startswith("ls"):
            try:
                stdin.split(" ")[1]
            except IndexError:
                lst = f"{os.path.abspath(os.getcwd())}"
                dr = os.path.abspath(os.getcwd())
            else:
                lst = stdin.split(" ")[1]
            for item in os.listdir(lst):
                if os.path.isdir(item):
                    item = f"{Color.RED}{item}{Color.END}"
                elif os.path.isfile(item):
                    item = f"{Color.GREEN}{item}{Color.END}"
                print(item)
        if stdin == "wd":
            print(pathlib.Path(__file__).parent.absolute())
        if stdin  == "..":
            os.chdir("..")


    except EOFError:
        print("")
        exit()
    except KeyboardInterrupt:
        print("")
        exit()
    else:
        pass
