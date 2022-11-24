class A:
    def __init__(self):
        print("In init A")
    def feature1(self):
        print("feature1 working")
    def feature2(self):
        print("feature2 working")
class B(A):
    def __init__(self):
        super().__init__()
        print("In init B")
    def feature3(self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")
# a1=A() #In init A
# b1=B() #In init A(In B, init is not present)
# b2=B()# In init B(no super)
b2=B()#In init A
# In init B