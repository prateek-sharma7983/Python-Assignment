class Vehicle:
    brand="BMW"
    color="red"
    def display(self):
        print("brand : " ,self.brand)
        print("color : " ,self.color)
class Car(Vehicle):
    model="A4"
    def show_car(self):
        c.display()
        print("model : ",self.model)
c=Car()
c.show_car()
    
                              