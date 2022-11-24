#Heap Memory contains objects
#size of an objects is dependent to no of variables and size of each variable
#constructor assign the memory to an object
class Computer:
    def __init__(self):
        self.name="Aditya Ranjan"
        self.age=24
    def update(self):
        self.age=40
    def compare(self,other):
        if self.age==other.age:
           return True
        else:
            return False
c1=Computer()
c2=Computer()
print(id(c1)) #2395004857104(address)
print(id(c2)) #2395004857232(address)
print(c1.name,c2.name) #Aditya Ranjan Aditya Ranjan
c1.name="Sonu Sharma"
print(c1.name,c2.name) #Sonu Sharma Aditya Ranjan
c1.update()
print(c1.age,c2.age) #40 24
if c1.compare(c2):
    print("They are same") 
else:
    print("They are different") #They are different
c2.update()
if c1.compare(c2):
    print("They are same")  #They are same
else:
    print("They are different")
