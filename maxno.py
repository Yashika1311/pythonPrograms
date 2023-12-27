# python program to find max of three 


num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")

elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")

elif num3 > num1 and num3 > num2:
    print(num3, "is the largest number")

else:
    print("Two or more numbers are equal")

