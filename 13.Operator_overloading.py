# Operator Overloading-operators are same but types of parameters passing or no of parameters 
# passing are  changed .
# a=1
# b=9
# print(a+b)
# print(int.__add__(a,b))
# x='1'
# y='4'
# print(x+y)
# print(str.__add__(x,y))
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False     
    def __str__(self):
        return f"{self.m1} , {self.m2}"
s1=Student(80,60)
s2=Student(70,30)
s3=s1+s2
print(s3.m1,s3.m2)# 150 90
if s1>s2: #s1 wins
    print("s1 wins")
else:
    print("S2 looses")
print(s1) #80 , 60