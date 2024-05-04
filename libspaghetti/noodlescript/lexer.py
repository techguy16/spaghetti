"""
NoodleScript Lexing Code for libspaghetti
"""
import libspaghetti
import libspaghetti.error
import libspaghetti.utils
import libspaghetti.variables

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
            lexed_line[2] = libspaghetti.utils.str2raw(lexed_line[2])
            
        if lexed_line[1] in supported_functions:
            return lexed_line
        else:
            return line
    elif line[0:6] == "noodle":
        var_info = line.split("noodle ")[1]
        if "=" in var_info:
            var_info = var_info.split(" = ")
            var_info.insert(0,"var")
            try:
                int(var_info[2])  # Try to convert the string to an integer
                var_info.insert(3,"int")
            except ValueError:
                var_info.insert(3,'str')
            return var_info
        else:
            if libspaghetti.variables.is_var(var_info):
                var_info = [f"{libspaghetti.variables.get_var_content(var_info)[0]}"]
                var_info.insert(0,"var")
                return libspaghetti.variables.get_var_content(var_info)
            else:
                return "e"
    elif line[0] == "#":
        if line[1] == " ":
            lexed_line = line.split("# ")
        else:
            lexed_line = line.split("#")
        lexed_line[0] = "comment"
        return lexed_line