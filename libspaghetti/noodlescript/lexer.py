"""
NoodleScript Lexing Code for libspaghetti
"""
import libspaghetti
import libspaghetti.error
import libspaghetti.utils

supported_functions = ["serve", "receive", "abs", "exit"]

def lex_line(line):
    """
    if "(\"" and "\")" in line:
        lexed_line = line.replace("(\"", "'split'").replace("\")", "'split'")
        if "'split'" in lexed_line:
            lexed_line = lexed_line.split("'split'")
            lexed_line.insert(0,"func")
            del lexed_line[-1]
        if lexed_line[1] in supported_functions:
            return lexed_line
        else:
            libspaghetti.error.undefined()
            return "err"
    el
    """
    if "(" and ")" in line:
        lexed_line = line.replace("(", "'split'", 1).replace(")", "'split'", -1)
        lexed_line = lexed_line.split("'split'")
        lexed_line = libspaghetti.utils.line_type(lexed_line, "func")
        
        if lexed_line[2][0] == "\"":
            lexed_line[2] = lexed_line[2][1:-1]
            
        if lexed_line[1] in supported_functions:
            return lexed_line
        else:
            libspaghetti.error.undefined()
            return "err"
    elif line[0:5] == "noodle":
        return "e"
    elif line[0] == "#":
        if line[1] == " ":
            lexed_line = line.split("# ")
        else:
            lexed_line = line.split("#")
        lexed_line[0] = "comment"
        return lexed_line