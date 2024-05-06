import sys

def parse_cli_arguments():
    return sys.argv[1:]

def get_file_to_run():
    if not len(sys.argv) == 1:
        if not sys.argv[1][0] == "-":
            return sys.argv[1]
        else:
            if not len(sys.argv) < 3:
                ind_count = 1
                while sys.argv[ind_count][0] == "-":
                    ind_count += 1
                return sys.argv[ind_count] 

def output_lexed_code():
    if len(sys.argv) > 1:
        if "-l" in sys.argv:
            ind_count = 1
            while not ind_count > len(sys.argv) and sys.argv[ind_count] != "-l":
                ind_count += 1
            if not ind_count > len(sys.argv) and sys.argv[ind_count] == "-l":
                return True
            else:
                return False
        else:
            return False
    else:
        return False