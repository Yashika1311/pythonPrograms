rows = int(input("Enter the number of rows: "))




for i in range(1, rows + 1):

    
    for j in range(i, rows):
        print(" ", end="")
    
    #             1,2,3      
    for j in range(1, 2 * i):
        print("*", end="")
    
    
    for j in range(2 * i, 2 * rows):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        print("*", end="")
    
    print()