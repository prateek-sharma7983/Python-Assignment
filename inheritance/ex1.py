class Person:
    name="Prateek"
    age=21
    
    def display(self):
       
        print("name : ",self.name)
        print("age : ",self.age)
class Student(Person):
    course="MCA"
    
    def show_details(self):
        print("course : " ,self.course)
        
s1=Student()
s1.display()
s1.show_details()