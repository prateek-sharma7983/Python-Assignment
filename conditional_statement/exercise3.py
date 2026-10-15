age=int(input("enter your age : "))
if age>=21:
    salary=int(input("enter your salary: "))
    if salary>=25000:
        credit_score=int(input("enter your credit_score : "))
        if credit_score>=750:
            print("loan approved : " )
        elif credit_score>=650:
            print("loan approved with higher interest : ")
        else:
            print("laon rejected: ")
    else:
        print("laon rejected: ")
else:
    print("laon rejected: ")