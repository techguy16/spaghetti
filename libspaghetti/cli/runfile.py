import libspaghetti.noodlescript.lexer
import libspaghetti.noodlescript.runner

def run_file(file):
    with open(file) as file:
        filelines = file.readlines()
    file.close()
    
    for line in filelines:
        libspaghetti.noodlescript.runner.run_line(libspaghetti.noodlescript.lexer.lex_line(line))