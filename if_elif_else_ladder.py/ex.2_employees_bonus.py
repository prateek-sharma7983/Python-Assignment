experience=int(input("enter your experience : "))
if experience>=1:
    salary=int(input("enter your salary : "))
    performance=int(input("enter your performance: "))
    if salary>=50000:
        
        if performance>=90:
            bonus=(salary*20)/100
        elif performance>=75:
            bonus=(salary*10)/100
        else:
             bonus=(salary*5)/100
    else:
        if performance>=90:
            bonus=(salary*200)/100
        else:
            bonus=(salary*200)/100
else:
    print("not eligible for bonus : ")
print("your got bonus of ", bonus ," rupees ")
