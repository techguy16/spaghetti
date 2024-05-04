from colorama import init as colorama_init # Col
from colorama import Fore                  # our
from colorama import Style                 # ama

colorama_init()

def unknown():
    print(f"{Style.BRIGHT}{Fore.RED}Unknown error{Style.RESET_ALL}")

def undefined(line=None):
    if line is not None:
        print(f"{Style.BRIGHT}{Fore.RED}Undefined function at line with code {Style.RESET_ALL}{Fore.RED}{line}")
    else:
        print(f"{Style.BRIGHT}{Fore.RED}Undefined function{Style.RESET_ALL}")
    
def syntax():
    print(f"{Style.BRIGHT}{Fore.RED}Syntax error{Style.RESET_ALL}")

# Legacy code for legacy systems
def error(type):
    if type.lower() == "syntax":
        return "Syntax error"
    else:
        return "Unknown error"