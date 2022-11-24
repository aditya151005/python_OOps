class A:
    def show(self):
        print("in A show")
class B(A):
     def show(self):#method overriding
        print("in B show")
# b1=B()
# b1.show() #in A show if A does not have show method
b2=B()
b2.show() #in B show