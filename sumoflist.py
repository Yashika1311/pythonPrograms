#Write a python function to sum all numbers in a list

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
list = [10, 20, 30, 40, 50]
result = sum(list)
print("The sum of numbers in list is:",result)  

