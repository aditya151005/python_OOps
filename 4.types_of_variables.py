class Car:
    wheels=5 #class/static variable
    def __init__(self):
        self.mil=10 #instance variable
        self.com="BMW" #instance variable
c1=Car()
c2=Car()
print(c1.mil,c1.com,c1.wheels) #10 BMW 5
print(c2.mil,c2.com,c2.wheels) #10 BMW 5
Car.wheels=3
print(c1.mil,c1.com,c1.wheels) #10 BMW 3
print(c2.mil,c2.com,c2.wheels) #10 BMW 3