sub1=int(input("enter marks of sub 1 : "))
sub2=int(input("enter marks of sub 2 : "))
sub3=int(input("enter marks of sub 3 : "))
if sub1>=40 and sub2>=40 and sub3>=40:
    per=(sub1+sub2+sub3)/3
    if per>=75:
        print("distinction : ")
    if per>=60:
        print("first division : ")
    if per>=50:
        print("second division : ")
    else:
        print("pass : ")
else:
    print("fail : ")
