
class A:
    def __init__(self,n):
        print(type(self))
        print("A Constructor")
        self.n = n

class B:
    def __init__(self,v):
        print("B Constructor")
        self.v = v

class C(A,B):
    def __init__(self,n,v):
        A.__init__(self,n)
        B.__init__(self,v)


obj = C(10,20)



