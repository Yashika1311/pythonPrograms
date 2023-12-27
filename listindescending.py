x=[76, 23, 45, 12, 54, 9] 
print("Original List:", x)

for i in range(7):
	for j in range(7):
		if x[i]>=                                                                                                   x[j]:
			x[i], x[j] = x[j],x[i]

print("Sorted List", x)
