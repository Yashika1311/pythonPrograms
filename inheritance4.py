class Parent:
    def add(self,x ,y):
        print(self.x + self.y)
    
class Child(Parent):
    def takevalue(self):
        self.x = int(input("Enter the value for x: "))
        print(self.x)
        self.y = int(input("Enter the value for y: "))
        print(self.y)
        return self.x,self.y 



obj = Child()

a,b = obj.takevalue()
obj.add(a,b)