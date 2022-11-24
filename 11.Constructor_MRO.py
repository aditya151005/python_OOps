class A:
    def __init__(self):
        print("In init A")
    def feature1(self):
        print("feature1_A working")
    def feature2(self):
        print("feature2 working")
class B():
    def __init__(self):
        print("In init B")
    def feature1(self):
        print("feature1_B working")
    def feature4(self):
        super().feature2()
        print("feature4 working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In init C")
    def feature4(self):
        super().feature2()
        print("feature4 working")
# c1=C()#MRO(left to right)
# In init A
# In init C
c1=C()
# c1.feature1()In init A
# In init C
# feature1_A working
# c1.feature4()
# In init A
# In init C
# feature2 working
# feature4 working