def reset():
    global variables
    variables = {}
    
def get_variables():
    global variables
    return variables 

def add_variable(name="var",data="",type="str",frozen="n"):
    global variables
    print(variables)
    if name in variables.keys():
        if variables[name][frozen] == "y":
            return "Cannot complete operation"
        else:
            variables[name] = [data, type, frozen]
    else:
        variables[name] = [data, type, frozen]
    
def is_var(name):
    global variables
    if name in variables:
        return True
    else:
        return False
    
def get_var_content(name):
    global variables
    if name in variables:
        return variables[name]
    else:
        return []