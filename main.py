import libspaghetti.noodlescript.lexer
import libspaghetti.version

print(libspaghetti.version.short())
print(libspaghetti.version.creator())
while True:
    line = input("> ")
    print(libspaghetti.noodlescript.lexer.lex_line(line))