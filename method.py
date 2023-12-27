#to demonstrate differnt methods of list

#step 1: creation of list

l=[1,2,3,4,5]
print(l)

#step 2: to use append to add one element at the end of the list

l.append(12)
print(l)

#step 3: to use extend to add multiple elements at the end of the list

l.extend([14,16])
print(l)

#step 4:to use pop to remove any i element from the list

l.pop(3)
print(l)

#step 5: to reverse to reverse the list

l.reverse()
print(l)

# step 6: to insert the item at perticular place

l.insert(3,90)
print(l)

# step7: to sort to descending order

l.sort(reverse=True)
print(l)

# step 8: to sort to ascending order

l.sort()
print(l)

