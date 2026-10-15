isavailable=input("is seat available  ? enter true or false : ").lower()=="true"
if(isavailable):
    age=int(input("enter your age : "))
    if(age<5 and age>0):
        print("you are free : ")
    elif(age>=5 and age<=12):
        print("you get 50'%' discount ")
    elif(age>60):
        print("30'%' discount ")
    else:
        print("full price")
else:
    print("seat full ")