import libspaghetti.noodlescript.lexer
import libspaghetti.noodlescript.runner
import libspaghetti.cli.parser

output_lexed_code = libspaghetti.cli.parser.output_lexed_code()

def run_file(file):
    with open(file) as file:
        filelines = file.readlines()
    file.close()
    
    for line in filelines:
        if output_lexed_code:
            if libspaghetti.noodlescript.lexer.lex_line(line) is not None:
                print(libspaghetti.noodlescript.lexer.lex_line(line))
        libspaghetti.noodlescript.runner.run_line(libspaghetti.noodlescript.lexer.lex_line(line))