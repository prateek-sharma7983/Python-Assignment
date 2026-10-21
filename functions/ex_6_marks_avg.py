def avg(*marks):
    if not marks:
        return "marks are not provided "
    for ex in marks:
        if not isinstance(ex,(int,float)) or isinstance(ex,bool):
           return "Provide only integer : "
        if ex<0 or ex>100:
            return "provide valid marks : "
    return sum(marks)/len(marks)
print(avg(55,66,77,88,99))
print(avg())
print(avg(55,66,True))
