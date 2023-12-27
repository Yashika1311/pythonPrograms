num=int(input("Enter number of rows: "))
# new=""
k=num-1
for i in range(num,0):
    for j in range(k,0):
        print(end=" ")
    k=k-1
    for j in range(i+1,0):
        print("* ",end="")
    print ("\r")