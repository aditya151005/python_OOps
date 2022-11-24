class Computer:
    def __init__(self,cpu,ram):#special method
          self.cpu=cpu
          self.ram=ram       
    def config(self):
        print("Config is:",self.cpu,self.ram)
com1=Computer('i5',16) 
com2=Computer('Rygen 3',8) 
com1.config() #Config is: i5 16
com2.config() #Config is: Rygen 3 8