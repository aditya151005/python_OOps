# polymorphism in python-
# 1.Duck Typing
# 2.Operator Overloading
# 3.Method Overloading
# 4.Method Overriding
# 1.Duck Typing-
# Duck Test-If Any bird looks like a duck,swim like a duck and quacks like a duck,
# then it probably is a duck
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self): #if there is an object ide and if it has a method execute that's it 
        #we are not concerned about which class method is it 
        print("spell check")
        print("convention check")
        print("Compiling")
        print("Running")        
class Laptop:
    def code(self,ide):
        ide.execute()
ide=PyCharm()
lap1=Laptop()
lap1.code(ide)#Compiling
# Running
ide=MyEditor()
lap1=Laptop()
lap1.code(ide)#spell check
# convention check
#Compiling
# Running

