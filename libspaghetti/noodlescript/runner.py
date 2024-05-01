def run_line(line):
    if line[0] == "func":
        if line[1] == "serve":
            print(line[2])
    else:
        print("error")