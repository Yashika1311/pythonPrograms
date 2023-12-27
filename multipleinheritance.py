class LU:
    def lets(self):
        LU = {1:'Sub= C++  Trainer = Sai Sir  Duration = 1month',
               2:"Sub = Java  Trainer = Prasad Sir  Duration = 3month", 
               3:"Sub = Python   Trainer = Saurabh Sir   Duration = 4month"}
        
class ITM:
    def itm(self):
        ITM = {1:"Sub = Maths   Trainer = Sumeet Sir  Duration = 1year ",
               2:"Sub = Physics Trainer = Kalpana Mam   Duration = 2year ",
               3:"Sub = Statistics  Trainer = Sheetal Mam  Duration = 1.5year"}
        
class Child(LU , ITM):
    def info(self):
        self.option=input("enter 'L' for Lets upgrade and 'I' for ITM" )
        if self.option=="L":
           print(LU.lets())

        elif self.option=="I":
            print(ITM.itm())

        elif self.option=="LI":
            print(LU.lets(),ITM.itm())

name=input("enter student name:")
age=int(input("Enter the age"))

obj= Child()
obj.info()