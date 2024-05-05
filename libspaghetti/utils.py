def line_type(line, type):
    line.insert(0,type)
    del line[-1]
    return line

def str2raw(str):
    return str[1:-1]

def str2int(str):
    return int(str)

def contentType(content):
    try:
        int(content)  # Try to convert the string to an integer
        return "int"
    except ValueError:
        if content == "true" or "True" or "false" or "False":
            return "bool"
        else:
            return "str"