num = int((input("enter the number")))


for i in range(1, num + 1 , 2):
    spaces = " " * ((num - i) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)


for i in range(num - 2, 0, -2):
    spaces = " " * ((num - i) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)