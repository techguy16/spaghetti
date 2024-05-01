"""
NoodleScript Lexing Code for libspaghetti
"""
from . import error
supported_functions = ["serve"]

def lex_line(line):
    if "(\"" and "\")" in line:
        lexed_line = line.replace("(\"", "'split'").replace("\")", "'split'")
        if "'split'" in lexed_line:
            lexed_line = lexed_line.split("'split'")
            lexed_line.insert(0,"func")
            del lexed_line[-1]
        if lexed_line[1] in supported_functions:
            return lexed_line
        else:
            return [error("UNKNOWN")]