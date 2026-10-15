employees={
    "Rahul":{"salary":60000,"experience":2},
    "Amit":{"salary":40000,"experience":5},
    "Priya":{"salary":70000,"experience":4},
    "Neha":{"salary":45000,"experience":6}

}


for name,data in employees.items():
    salary=data["salary"]
    exp=data["experience"]
    if salary>=50000:
        if exp>=5:
            print("senior employees")
        else:
            print("mid level employee")
    else:
        if exp>=3:
            print("experienced junior :")
        else:
            print("fresher")
            