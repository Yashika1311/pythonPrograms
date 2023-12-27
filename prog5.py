#take list of strings as input and sort them based on their length


listinput = input("Enter a list of strings: ").split()

listinput.sort(key=len)

print("Sorted list based on string length: ", listinput)