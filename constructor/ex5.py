class Product:
    def __init__(self,product,price,quantity=1):
        self.product=product
        self.price=price
        self.quantity=quantity
    def showdetails(self):
        print("product : " , self.product)
        print("price : " , self.price)
        print("quantity : " , self.quantity)
p1=Product("Laptop",50000,2)
p1.showdetails()
print(" ")
p2=Product("Mouse",500)
p2.showdetails()

