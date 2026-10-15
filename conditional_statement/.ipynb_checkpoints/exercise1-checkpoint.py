
pin=int(input("enter your pin : "))
if pin==123:
    with_amount=int(input("enter amount you want to withdraw : "))
    if with_amount%100==0:
        if with_amount<=20000:
            print(with_amount, "amount withdraw")
            print((20000-with_amount),"is remaining")
        else:
            print("unsufficient balance")
    else:
        print("enter valid amount : ")
else:
    print("enter valid pin : ")