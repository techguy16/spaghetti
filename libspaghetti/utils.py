def line_type(line, type):
    line.insert(0,type)
    del line[-1]
    return line

def str2raw(str):
    return str[1:-1]

def str2int(str):
    return int(str)