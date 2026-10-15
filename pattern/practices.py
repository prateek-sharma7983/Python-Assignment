list=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for el in list:
    if el%2==0:
        even.append(el)
        
    else:
        odd.append(el)
print(even)
print(odd)