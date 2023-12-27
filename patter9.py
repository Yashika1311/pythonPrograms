val=66
for i in range(3,5):
    for j in range(0,i+1):
        ch=chr(val)
        print(ch,end=" ")
    val=val+1
    print()
