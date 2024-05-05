import libspaghetti
import libspaghetti.error
import libspaghetti.variables

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
        elif line == "e":
            print("Variables in dev")
        elif line[0] == "var":
            libspaghetti.variables.add_variable(line[1], line[2], line[3])
        elif line[0] == "varReturnInfo":
            print(line[1])
        else:
            return libspaghetti.error.undefined(line)
    else:
        return libspaghetti.error.undefined()