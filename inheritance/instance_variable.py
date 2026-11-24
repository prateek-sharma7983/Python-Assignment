class Employee:
    company_name="infosys"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print(self.name, " : " , self.salary)
    @classmethod
    def get_infor(cls):
        print(cls.company_name)
e1=Employee("Prateek",100000)
e1.details()
e1.get_infor()
print(Employee.company_name)