def employee_details(**kwargs):
    for key,value in kwargs.items():
        print(key," : ", value)

employee_details(name="Prateek",department="IT",salary="50000",city="Bareilly",experience="0-1")