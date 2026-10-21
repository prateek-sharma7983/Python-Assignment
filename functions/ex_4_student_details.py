def student_details(name,*marks,**kwargs):
    print("name : ",name)
    print("marks : ",marks)

    if len(marks)>0:
        total=sum(marks)
        avg=total/len(marks)
        print("total marks are : ",total)
        print("avg of marks is : ",avg)
    print("ADDITIONAL INFORMATION : ")
    for key ,value in kwargs.items():
        print(key, " :",value)

student_details("Prateek",89,98,80,96,rollnumber=80,sem="1st")