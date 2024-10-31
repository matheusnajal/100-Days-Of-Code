from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
       "-": subtract, 
       "*": multiply, 
       "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    while True:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number: "))
        answer = operations[operation_symbol] (num1, num2)
        print(f"{num1:.2f} {operation_symbol} {num2:.2f} = {answer:.2f}")

        choice = input(f"Type 'y' to continue calculating with {answer:.2f}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            os.system('cls')
            calculator()
            break

calculator()