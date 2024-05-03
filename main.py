import libspaghetti.noodlescript.lexer
import libspaghetti.noodlescript.runner
import libspaghetti.version

print(f"{libspaghetti.version.short()}\nRunning on Python {libspaghetti.version.python_ver()}\n{libspaghetti.version.creator()}\n")

while True:
    line = input("> ")
    libspaghetti.noodlescript.runner.run_line(libspaghetti.noodlescript.lexer.lex_line(line))