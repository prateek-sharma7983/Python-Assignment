list=[1,2,3,4,5,6,7,8,9]

n=int(input("enter the number you have to found : "))
found=0
ind=0
for el in list:
    

    if el==n:
        print("found at: ",ind)
        found+=1
        break
    ind+=1
if found==0:
    print("not found : ")