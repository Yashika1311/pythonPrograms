class parent:
    property=(800)
    print("The property which will be inherited generation to generation will be:",property,"$")
    property2=()

class generation1(parent):
    added_property=(int(input("enter Cost of Property by Father:")))
    p=(parent.property+added_property)
    print("Total Cost of Property owned by Father is:",p,"Rs")

class generation2(generation1):
    added__property=(int(input("enter the cost of property owned by son:")))
    s=(generation1.p+added__property)

c=generation2.s
print("The Total price of property son will get is:",c,"Rs")