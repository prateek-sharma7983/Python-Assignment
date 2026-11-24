class student:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print(f"the name is {self.name} : salary is {self.salary}")
        

s1=student("Prateek",1000000)
print(s1.__dict__)
