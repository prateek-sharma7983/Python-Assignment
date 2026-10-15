students={
    "Rahul":{"marks":85,"attendence":90},
    "Amit":{"marks":35,"attendence":80},
    "Priya":{"marks":65,"attendence":70},
    "Neha":{"marks":45,"attendence":85},
    "Rohit":{"marks":90,"attendence":60}

}

for name , data in students.items():
    att=data["attendence"]
    marks=data["marks"]

    if att<75:
        print(name, " Not Eligible : ")
    else:
        if marks>=80:   
            print(name , "Distinction : ")
        elif marks>=60:
                    print(name , "First Division : ")
        elif marks>=40:
                    print(name , "pass : ")
        else:
               print(name, "Fail")

