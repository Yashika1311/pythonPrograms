d={1:'hello','two':42,'blah':[1,2,3],dict:{1:'flower',2:'red'}}
print(d)
print(d['blah'])
print(d[1])
print(d['two'])
d[2]=(12)
print(d)
d['blah'].append(5)
print(d)
del(d[dict][1])
print(d)
