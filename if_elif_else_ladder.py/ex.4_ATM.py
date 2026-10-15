# pin=int(input("enter your pin : "))
# isaccount_active=True
# balance=30000
# if pin==12345:
#     if isaccount_active==True:
#         amount=int(input("enter you amount : "))
#         if amount>0:
#             if amount>20000:
#                 print("extra verifications : ")
#             elif(amount%100==0):
#                 rem_amount=balance-amount
#                 if rem_amount>=500:
#                     print(amount, " is withdraw succesfully :\n",rem_amount,"is remaining amount : ")
#                 else:
#                     print("the remaining amount is less than 500 , you can not withdraw\nenter 500 less from amount")
#             else:
#                 print("enter valid amount : ")
#         # elif amount>20000:
#         #     print("extra verifications : ")
#         else:
#             print("not valid : ")
#     else:
#         print("acount is not active : ")
# else:
#     print("pin is incorrect : ")




pin=input("enter your pin ")
balance=30000
if pin=="123":
    is_active=input("is account acvtive ? yes/no").lower()=="yes"
    if is_active:
        amount=int(input("enter your amount : "))
        if amount>0 and amount%100==0:
            if amount>20000:
                print("extra verification : ")
            else:
                rem_amount=balance-amount
                if balance>=500:
                    print("withdraw : ")
                else:
                    print("rem amount is less sthan 500 : cant withdraw : ")
        else:
            print("enter valid amount : ")
    else:
        print("acount is not active :")
else:
    print("wrong pin ")

print("you withdraw ",amount)
print("ramaining amoubnt is ",rem_amount)



    
    