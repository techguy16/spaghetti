def line_type(line, type):
    line.insert(0,type)
    del line[-1]
    return line