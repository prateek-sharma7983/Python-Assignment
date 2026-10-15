cart_amount=int(input("enter you cart amount "))
is_premium=input("are you a premium member : yes/no ").lower()
is_premium=is_premium=="yes"
if cart_amount>=5000:
    if is_premium==True:
        discount=(cart_amount*20)/100
    else:
        discount=(cart_amount*10)/100
else:
    if is_premium==True:
        discount=(cart_amount*5)/100
    else:
        print("no discount : ")
print("your total amount is   : ",cart_amount)
print("your total discount is : ",discount)
print("now you have to pay    : ",cart_amount-discount)


