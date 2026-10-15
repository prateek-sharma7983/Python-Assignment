username=input("enter your username : ").lower()
if username=="prateek":
    password=input("enter your password : ")
    if password=="7983":
        role=input("enter your role : ").lower()
        if role=="admin":
            print("full access:")
        elif role=="teacher":
            print("Teacher Dashboard : ")
        elif role=="student":
            print("Students Dashboard : ")
        else:
            print("invalid role :")
    else:
        print("wrong password : ")
else:
    print("invalid username :")

