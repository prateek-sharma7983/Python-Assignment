accounts={
    "Rahul":25000,
    "Amit":5000,
    "Priya":0,
    "Neha":-2000
}


for name,balance in accounts.items():
    if balance==0:
        print("no balance : ")
    elif balance>0:
        if balance>=10000:
            print("premium account")
        else:
            print("regular account")
    else:
        print("overdraft")