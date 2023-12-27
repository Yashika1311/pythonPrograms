#prog that creates dictionary of cubes of odd no in the range 1-10

d = {}
for x in range(1, 11, 2):
    d[x] = x**3
print(d)