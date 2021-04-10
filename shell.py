import os

lin_home = "/home/daniel"

class color:
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
    stdin = input(f"{color.BOLD}{os.path.abspath(os.getcwd()).replace(lin_home, '~')}{color.END}\n(> ")
    if stdin == "exit":
        exit()
    if stdin == "clear":
        os.system('clear')
    if stdin == "help":
        print("""Commands:
    clear       Clears screen.
    exit        Exits shell.
    help        Shows this message.""")