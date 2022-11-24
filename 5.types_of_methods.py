class Student:
    school="Hellens School"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self): #instance method(1.Accesser method(to fetch the value),2.mutator(to set the value))
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=100
    @classmethod
    def getschool(cls): #class method
        return cls.school
    @staticmethod
    def info():
        print("This is static methods .....")
            
s1=Student(60,40,20)
s2=Student(90,30,30)
print(s1.avg()) #40.0
print(s2.avg()) #50.0
print(s1.get_m1()) #60
s2.set_m1(100)
print(s2.get_m1()) #100
print(Student.getschool()) #Hellens School
Student.info() #This is static methods .....