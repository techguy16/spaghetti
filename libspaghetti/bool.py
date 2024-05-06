def boolean_parser(firstItem,operator,secondItem):
    if operator == "==":
        if firstItem == secondItem:
            return True
        else:
            return False
    elif operator == "!=":
        if firstItem != secondItem:
            return True
        else:
            return False
    elif operator == ">":
        if firstItem > secondItem:
            return True
        else:
            return False
    elif operator == "<":
        if firstItem < secondItem:
            return True
        else:
            return False
    else:
        return False