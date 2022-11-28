# by default, python does not support abstract methods and abstract class. To create abstract 
# methods and  abstract class we need abc module.(abstract base class)
#abstract method-A method which does not have definition but only have declaration.
#abstract class- A classs which has atleast one abstract methods is called abstract class.
#we can't create object of abstract class.
from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
     def process(self):
        print("Running")    
l=Laptop()
l.process() #Running