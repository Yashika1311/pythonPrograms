class Parent:
    def area(self, x, y = None):
        if y is None:
            return x * x
        else:
            return x * y

class Child(Parent):
    def take_values(self):
        self.option = int(input("Enter 1 for square or 2 for rectangle: "))
        if self.option == 1:
            self.x = float(input("Enter the length of side for area of square: "))
        elif self.option == 2:
            self.x = float(input("Enter the length for area of rectangle: "))
            self.y = float(input("Enter the breadth for area of rectangle: "))
        else:
            print("Invalid Option")

obj = Child()
obj.take_values()

if obj.option == 1:
    print("Area of the square is: ", obj.area(obj.x))
elif obj.option == 2:
    print("Area of the rectangle is: ", obj.area(obj.x, obj.y))