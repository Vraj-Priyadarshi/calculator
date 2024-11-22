from replit import clear
from art import logo 



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary mapping operation symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator ():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    shouldcontinue = True
    while shouldcontinue:
        operation_symbol = input("Pick an operation from the above list: ")
        operational_function = operations[operation_symbol]
        num2 = float(input("Enter next number: "))
        answer = operational_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        conti = input(f"Do you want ot continue with {answer} type 'Y' or if you want ot exit type 'N' ")
        continous = conti.lower()
        if continous == "y":
            num1 = answer
        else:
            shouldcontinue = False
            clear()
            calculator()

calculator()