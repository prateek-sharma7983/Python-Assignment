class Computer:
    def __init__(self):
        self.ram="8gb"
        self.storage="512gb"
        printf("the Computer class constructor")
class Mobile:
    def __init__(self):
        self.model="Iphone"
        print("child class constructor ")
M=Mobile()
print(M.__dict__)