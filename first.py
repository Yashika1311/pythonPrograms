print("module name of first",__name__)
def add(x,y):
    print(x+y)
if __name__=='__main__':
    add(3,7)
else:
    print("Module name of mumodule after import:",__name__)
    print("Mymodule is imported")