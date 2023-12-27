class Parent:
    def add (self, x, y):
        return self.x + self.y
    
class Child(Parent):
    def takevalue(self, x, y):
        result = self.add (x, y)
        print ("Result: ", result)

x = int(input("Enter the value for x : "))
y = int(input("Enter the value for y : "))

child_instance = Child()

child_instance.takevalue(x, y)