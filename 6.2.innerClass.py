class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=10  
        def show(self):
          print(self.brand,self.cpu,self.ram)      
s1=Student("Aditya",34)
s2=Student("Sonu",50)
s1.show() #Aditya 34
#HP i5 10 
s2.show() #Sonu 50
#HP i5 10
