class area:
    def area(self,x ):
        return x*x
    
class Child(area):
    def takevalue(self):
        a = float(input("Enter the value: "))
        self.x = a
        print("The result is:", a)

obj = Child()
obj.takevalue()
print(obj.area(obj.x))