import libspaghetti.cli.runfile
import libspaghetti.noodlescript.lexer
import libspaghetti.noodlescript.runner
import libspaghetti.cli.parser
import libspaghetti.version

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

if libspaghetti.cli.parser.get_file_to_run() is not None:
    print(f'Running file {libspaghetti.cli.parser.get_file_to_run()}')
    libspaghetti.cli.runfile.run_file(libspaghetti.cli.parser.get_file_to_run())
else:
    print(f"{Style.BRIGHT}{Fore.BLUE}{libspaghetti.version.short()}\nRunning on Python {libspaghetti.version.python_ver()}\n{Style.RESET_ALL}{libspaghetti.version.creator()}\n")

    while True:
        line = input(f"{Fore.MAGENTA}> {Fore.RESET}")
        libspaghetti.noodlescript.runner.run_line(libspaghetti.noodlescript.lexer.lex_line(line))