students={
    "Rahul":{"attendence":85,"marks":70},
    "Amit":{"attendence":60,"marks":80},
    "Priya":{"attendence":90,"marks":35},
    "Neha":{"attendence":78,"marks":55}

}

for name,data in students.items():
    attendence=data["attendence"]
    marks=data["marks"]
    if attendence>=75:
        if marks>=40:
            print("Eligible")
        else:
            print("Failed in exams")
    else:
        print("not eligible")


