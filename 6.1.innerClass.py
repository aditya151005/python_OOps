class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=10        
s1=Student("Aditya",34)
s2=Student("Sonu",50)
s1.show()
s2.show()
lap1=s1.lap
lap2=s2.lap
print(id(lap1))#2391642864080
print(id(lap2))#2391642864208 
lap3=Student.Laptop()
print(id(lap3))# 2939376171728
