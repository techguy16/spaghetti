import libspaghetti
import libspaghetti.error

def run_line(line):
    if not line == None:
        if line[0] == "func":
            if line[1] == "serve":
                print(line[2])
            elif line[1] == "receive":
                receive = input(line[2])
                print(receive)
            elif line[1] == "abs":
                print(abs(int(line[2])))
        elif line[0] == "comment":
            return "" 
        else:
            return libspaghetti.error.undefined()
    else:
        return libspaghetti.error.undefined()