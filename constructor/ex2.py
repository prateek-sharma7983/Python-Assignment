class Parent:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def display(self):
        print("name is : " ,self.name)
        print("age is : " ,self.age)
class Employee(Parent):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def show_employee(self):
        print("name is : " ,self.name)
        print("age is : " ,self.age)
        print("salary is : " ,self.salary)

E1=Employee("Prateek",21,1000000)
E1.display()
print("="*30)
E1.show_employee()
