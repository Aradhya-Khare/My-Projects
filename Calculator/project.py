def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    number1 = float(int(input("Enter the first number: ")))
    for keys in operations:
        print(keys)

    calculation_over = False
    while not calculation_over:
        value = input("Select an operation: ")
        number2 = float(int(input("Enter another number: ")))
        operator = operations[value]
        ans = round(operator(number1, number2), 2)
        print(F"{number1} {value} {number2} = {ans}")

        a = input(f"Enter 'y' to continue calculating with {ans} or enter 'n' to stop calculating, if you want to start calculating from begining then type 're': ").lower()
        if a == 'y':
            number1 = ans
        elif a == 're':
            calculation_over = True
            calculator()
        elif a == 'n':
            calculation_over = True
        else:
            print("Invalid input")

calculator()



