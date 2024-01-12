def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation_choice = input("Select operation (1/2/3/4): ")

    if operation_choice not in {'1', '2', '3', '4'}:
        print("Invalid operation choice")
        return

    x = float(input("Enter first operand: "))
    y = float(input("Enter second operand: "))

    if operation_choice == '1':
        result = add(x, y)
        print(f"{x} + {y} = {result}")
    elif operation_choice == '2':
        result = subtract(x, y)
        print(f"{x} - {y} = {result}")
    elif operation_choice == '3':
        result = multiply(x, y)
        print(f"{x} * {y} = {result}")
    elif operation_choice == '4':
        result = divide(x, y)
        print(f"{x} / {y} = {result}")

# Run the calculator
calculator()
