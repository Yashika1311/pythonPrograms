class Parent:
    def area(self, x):
        return x * x

class Child(Parent): 

    def takevalue(self):
        a = float(input("Enter the value: "))
        self.x = a
        print("The result is:", a)

obj = Child()  
obj.takevalue()
print("Area of the square is", obj.area(obj.x))