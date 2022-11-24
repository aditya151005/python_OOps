# python supports different programming paradigm-
# 1.procedure oriented programming(different modules will be a function)
# 2.functional programming
# 3.oop
# object is an instance of the class.
# object has an attributes(variables) and behaviour(function/methods)
# class is the blueprint of the object.
# creating the class-
class Computer:
    def config(self):
        print("i5,16gb,1TB")
com1=Computer()
com2=Computer()
print(type(com1)) #<class '__main__.Computer'>
Computer.config(com1) #i5,16gb,1TB
Computer.config(com2) #i5,16gb,1TB
com1.config()  #i5,16gb,1TB
com2.config()   #i5,16gb,1TB