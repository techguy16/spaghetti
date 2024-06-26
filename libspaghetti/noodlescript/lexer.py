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
    if line is not None:
        if "(" and ")" in line:
            if "(noodle " in line:
                line_mod = line.split("(noodle ")[1].split(")")
                del line_mod[1]
                replace_with = libspaghetti.variables.get_var_content(line_mod[0])[0]
                to_replace = f"noodle {line_mod[0]}"
                lexed_line = line.replace(to_replace, replace_with)
            else:
                lexed_line = line
            lexed_line = lexed_line.replace("(", "'split'", 1).replace(")", "'split'", -1)
            lexed_line = lexed_line.split("'split'")
            lexed_line = libspaghetti.utils.line_type(lexed_line, "func")
        
            if lexed_line[2][0] == "\"":
                lexed_line[2] = libspaghetti.utils.str2raw(lexed_line[2])
            
            if lexed_line[1] in supported_functions:
                return lexed_line
            else:
                return line
        elif (line[0:6] == "noodle") or (line[0:13] == "frozen noodle"):
            if line[0:13] == "frozen noodle":
                var_info = line.split("frozen noodle ")[1]
            else:
                var_info = line.split("noodle ")[1]
            var_split = var_info.split(" ")
            if not len(var_split) == 1:
                var_info = var_info.split(" = ")
                var_info.insert(0,"var")
                try:
                    int(var_info[2])  # Try to convert the string to an integer
                    var_info.insert(3,"int")
                except ValueError:
                    var_info.insert(3,'str')
                if line[0:13] == "frozen noodle":
                        var_info.insert(4, "frozen")
                return var_info
            else:
                if libspaghetti.variables.is_var(var_info):
                    var_info = libspaghetti.variables.get_var_content(var_info)
                    if not var_info[0] == "varReturnInfo":
                        var_info.insert(0,"varReturnInfo")
                    if line[0:13] == "frozen noodle":
                        if not "frozen" in var_info:
                            var_info.insert(4, "frozen")
                    return var_info
                else:
                    var_info = libspaghetti.variables.get_var_content(var_info)
                    return var_info

        elif line[0] == "#":
            if line[1] == " ":
                lexed_line = line.split("# ")
            else:
                lexed_line = line.split("#")
            lexed_line[0] = "comment"
            return lexed_line