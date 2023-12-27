p = x = int(input("Enter Number 1: "))
q = y = int(input("Enter Number 2: "))

while x != y:   
  if x > y:
    x = x - y
  else:
    y = y - x

lcm = (p*q)/x

print("The LCM is: ", lcm)
