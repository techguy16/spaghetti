import libspaghetti.cli.runfile
import libspaghetti.noodlescript.lexer
import libspaghetti.noodlescript.runner
import libspaghetti.cli.parser
import libspaghetti.variables
import libspaghetti.version

from colorama import init as colorama_init # Col
from colorama import Fore                  # our
from colorama import Style                 # ama

colorama_init()

libspaghetti.variables.reset()

output_lexed_code = libspaghetti.cli.parser.output_lexed_code()

if libspaghetti.cli.parser.get_file_to_run() is not None:
    print(f'{Style.BRIGHT}{Fore.BLUE}> {Style.RESET_ALL}{Fore.GREEN}Running file {Style.BRIGHT}"{libspaghetti.cli.parser.get_file_to_run()}"{Style.RESET_ALL}')
    libspaghetti.cli.runfile.run_file(libspaghetti.cli.parser.get_file_to_run())
else:
    print(f"{Style.BRIGHT}{Fore.BLUE}{libspaghetti.version.short()}\nRunning on Python {libspaghetti.version.python_ver()}\n{Style.RESET_ALL}{libspaghetti.version.creator()}\n")

    while True:
        line = input(f"{Fore.MAGENTA}> {Fore.RESET}")
        if output_lexed_code:
            print(f"{Fore.BLUE}{str(libspaghetti.noodlescript.lexer.lex_line(line)).replace('\',', ",\n")}{Fore.RESET}\n")
        libspaghetti.noodlescript.runner.run_line(libspaghetti.noodlescript.lexer.lex_line(line))