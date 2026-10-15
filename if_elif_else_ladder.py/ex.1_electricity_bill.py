unit=int(input("enter your unit "))
if(unit<=100 and unit>0):
    bill=unit*5

elif(unit>100 and unit<=200):
    bill=unit*7
elif(unit>200 and unit<=300):
    bill=unit*10
elif(unit>300):
    bill=unit*15
else:
    print("enter valid unit ")
if(bill>3000):
    surcharge=(bill*10)/100
    print("your total units are\n",unit, "your total bill is\n", bill, "you have to pay surcgarge of\n",surcharge)
   
else:
    print("your total units are\n", unit,"your total bill is ", bill)