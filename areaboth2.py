class AreaCalculator:
    def _init_(self):
        self.length = 0
        self.width = 0

    def get_user_input(self):
        self.length = int(input("Enter the length: "))
        self.width = int(input("Enter the width : "))

    def calculate_square_area(self):
        return self.length * self.length

    def calculate_rectangle_area(self):
        return self.length * self.width

    def display_results(self, shape):
        if shape == "square":
            area = self.calculate_square_area()
        elif shape == "rectangle":
            area = self.calculate_rectangle_area()
        else:
            print("Invalid shape specified")

        print(f"Area of {shape} is: {area}")

calculator = AreaCalculator()

shape_choice = input("Enter the shape (square/rectangle): ").lower()
calculator.get_user_input()

if shape_choice == "square":
    calculator.display_results("square")
elif shape_choice == "rectangle":
    calculator.display_results("rectangle")
else:
    print("Invalid shape specified. Please enter 'square' or 'rectangle'.")
