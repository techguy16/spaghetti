def math_parser(first_number, first_operator, second_number, second_operator, third_number):
    math_working = []
    if first_operator == "/" or "*":
        math_working.insert(0, first_number)
        math_working.insert(1, first_operator)
        math_working.insert(2, second_number)