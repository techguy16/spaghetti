"""
NoodleScript Lexing Code for libspaghetti
"""

def lex_line(line):
    lexed_line = line.replace("(\"", "'split'").replace("\")", "'split'")
    if "'split'" in lexed_line:
        lexed_line = lexed_line.split("'split'")
        lexed_line.insert(0,"func")
        del lexed_line[-1]
    return lexed_line