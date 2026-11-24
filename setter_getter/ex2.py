class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def setsalary(self,salary):
        if salary>0:
            self.salary=salary
        else:
            print("invalid salary")
    def getsalary(self):
        return self.salary
e1 = Employee("Rahul", 25000)
print(e1.salary)

print(e1.getsalary())

e1.setsalary(35000)
print(e1.getsalary())

e1.setsalary(-5000)
print(e1.getsalary())