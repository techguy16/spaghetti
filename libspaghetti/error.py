def unknown():
    print("Unknown error")

def undefined():
    print("Undefined function")
    
def syntax():
    print("Syntax error")

# Legacy code for legacy systems
def error(type):
    if type.lower() == "syntax":
        return "Syntax error"
    else:
        return "Unknown error"