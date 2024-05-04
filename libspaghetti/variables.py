def reset():
    global variables
    variables = {}
    
def get_variables():
    return variables 

def add_variable(name="var",data="",type="str"):
    variables[name] = [data, type]
    
def is_var(name):
    if name in variables:
        return True
    else:
        return False
    
def get_var_content(name):
    if name[1] in variables:
        return variables[name]
    else:
        return []