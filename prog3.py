print("-------WELCOME TO PARKING--------")


name=(str(input("Enter your name")))
car=(int(input("Enter your car number")))
print("PLEASE ENTER THE TYPE OF VEHICAL")
print("'C' for car, 'B' for bus,'T' for truck,'S' for scooty")
ch=input("Enter the type of vehical:")[0].upper()
timecheckin=(float(input("Enter checkin time:")))
timecheckout=(float(input("Enter checkout time:")))
timediff=(timecheckout-timecheckin)

if ch=='C':
    if timediff>3:
     print("Name of Car owner is: ",name)
     print("Name of Car is:",car)
     print("Checkin Time is:",timecheckin)
     print("Checkout Time is:",timecheckout)
     print(5*timediff,"RS you will have to pay")
    elif timediff<=3 and timediff>=0:
       print("Name of Car owner is: ",name)
       print("Name of Car is:",car)
       print("Checkin Time is:",timecheckin)
       print("Checkout Time is:",timecheckout)
       print("You will have to pay RS 10")

elif ch=='B':
   if timediff>3:
      print("Name of Car owner is: ",name)
      print("Name of Car is:",car)
      print("Checkin Time is:",timecheckin)
      print("Checkout Time is:",timecheckout)
      print(10*timediff,"RS you will have to pay")
elif timediff<=3 and timediff>=0:
       print("Name of Car owner is: ",name)
       print("Name of Car is:",car)
       print("Checkin Time is:",timecheckin)
       print("Checkout Time is:",timecheckout)
       print("You will have to pay RS 20") 
   

elif ch=='T':
    if timediff>3:
       print("Name of Car owner is: ",name)
       print("Name of Car is:",car)
       print("Checkin Time is:",timecheckin)
       print("Checkout Time is:",timecheckout)
       print(10*timediff,"RS You will have to pay")
    elif timediff<=3 and timediff>=0:
       print("Name of Car owner is: ",name)
       print("Name of Car is:",car)
       print("Checkin Time is:",timecheckin)
       print("Checkout Time is:",timecheckout)
       print("You will have to pay RS 20")

elif ch=='S':
    if timediff>3:
       print("Name of Car owner is: ",name)
       print("Name of Car is:",car)
       print("Checkin Time is:",timecheckin)
       print("Checkout Time is:",timecheckout) 
       print(2.5*timediff,"RS You will have to pay")
    elif timediff<=3 and timediff>=0:
       print("Name of Car owner is: ",name)
       print("Name of Car is:",car)
       print("Checkin Time is:",timecheckin)
       print("Checkout Time is:",timecheckout)
       print("You will have to pay RS 5")

else:
   ("invalid")










