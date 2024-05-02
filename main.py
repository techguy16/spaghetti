import libspaghetti.noodlescript.lexer
import libspaghetti.noodlescript.runner
import libspaghetti.version

print(libspaghetti.version.short())
print(libspaghetti.version.creator())
print()

while True:
    line = input("> ")
    libspaghetti.noodlescript.runner.run_line(libspaghetti.noodlescript.lexer.lex_line(line))