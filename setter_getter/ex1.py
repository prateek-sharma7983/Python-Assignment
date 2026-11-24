class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def setMarks(self,marks):
        if 0<=marks<=100:
            self.marks=marks
        else:
            print("invalid marks")
    def getMarks(self):
        return self.marks
s1=Student("Prateek",90)
print(s1.getMarks())
s1.setMarks(120)
print(s1.getMarks())
