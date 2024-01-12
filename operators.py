#Aim:To demonstrate  arithmatic operators
print("WELCOME TO THE MATHS world")
print("Here you can learn more about maths different operations where you can get the answers ......")
print("what kind of operation you want to perform")
print("1-for arithmetic ,2-forRelational,3-for logical,4-for bitwise,5-for ternery,6-for membership,7-for identity ")
operation=int(input("enter the operation number"))
if operation==1:
 print("enter 1-for addition,2-for subtraction,3-for multiplication,4-for division,5-for floor division,6-for modulus,7-for exponential ")
x=int(input("enter the operation number"))
a=float(input("Enter first num:"))
b=float(input("Enter second  num:"))


if x == 1:
    print("sum of two number is",a+b)
elif x==2:
    print("sub of two no is",a-b)
elif x==3:
    print("multiplication of two num is",a*b)
elif x==4:
    print("div of two num is",a/b)
elif x==5:
    print("floordivision of two num is",a//b)
elif x==6:
    print("modulus of two num is",a%b)
elif x==7:
    print("exponential of two num is",a**b)


elif operation==2:
     print("Here you will get to know more about RELATIONAL OPERATION")
     print ("lets see if the given numbers  by you are what??? ")

     number1=float(input("Enter the first number"))
     number2=float(input("Enter the second number"))

     if number1==number2:
         print("Both the number are EQUAL")
     elif number1>number2:
         print("Number 1 is GREATER and Number 2 is SMALLER")
     elif number2>number1:
         print("Number 2 is GREATER and Number 1 is SMALLER")
     elif number1!=number2:
         print("Both NUMBERS are not EQUAL")

elif operation==3:
    print("Here we will be doing ASSGNMENT OPERATIONS")
    print("Please enter 2 number for following operations")
    print("1-for +=,2-for -=,3-for *=,4-for /=,5-for floordivison equal to,6-for modulas equal to,7-for exponentional equal to ")

    op=int(input("enter the operation you wnat in ASSIGNMENT"))
    p=float(input("Enter the first number"))
    q=float(input("Enter the second number"))

if op==1:
    print(p=p+q)
    

     






