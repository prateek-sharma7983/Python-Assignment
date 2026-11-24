#simple inheritance:

class Parent:
    def display(self):
        print("i am parent class :")
class Child(Parent):
    def show(self):
        print("i am child class : ")
c=Child()
c.display()
c.show()
        