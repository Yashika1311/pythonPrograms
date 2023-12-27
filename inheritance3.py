class addition:
    def add(self, a, b):
        return a + b

class user_input(addition):
    def get_user_input(self):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2


user_input_adder = user_input()
numbers = user_input_adder.get_user_input()
result = user_input_adder.add(*numbers)
print(f"The sum of {numbers[0]} and {numbers[1]} is: {result}")