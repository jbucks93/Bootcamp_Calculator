
from calc_art import logo
print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    
    n1 = int(input("First number: "))
    operator_choice = input("Pick operation: ") 
    n2 = int(input("Second number: "))

    math_function = operations[operator_choice]
    first_answer = math_function(n1,n2)

    print(f"{n1} {operator_choice} {n2} = {first_answer}")
    continue_calc = input(f"type y to use {first_answer} or n to restart")
    if continue_calc == "y":
        new_calculator(first_answer)
    else:
        calculator()

def new_calculator(x):

    operator_choice = input("Pick operation: ")
    n3 = int(input("What's the next number?: "))

    math_function = operations[operator_choice]
    second_answer = math_function(x, n3)

    print(f"{x} {operator_choice} {n3} = {second_answer}")
    continue_calc = input(f"type y to use {second_answer} or n to restart")
    
    if continue_calc == "y":
        first_answer = second_answer
        new_calculator(first_answer)
    else:
        calculator()

calculator()