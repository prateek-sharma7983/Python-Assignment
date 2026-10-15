"""
0
1 0
0 1 0
1 0 1 0
0 1 0 1 0
"""
n=int(input("enter the numbers of rows : "))
for i in range(0,n):
    for j in range(0,i+1):
        print((i+j)%2, end=" ")
    print("\n")