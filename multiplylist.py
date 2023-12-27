#multiplication of numbers in list

def multiple(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
list= [10, 20, 30, 40, 50]
result = multiple(list)
print(result)  