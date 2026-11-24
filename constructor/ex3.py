class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Child(Parent):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course
ob=Child("Prateek",18,"mca")
print(ob.course)
print(ob.name)
print(ob.age)