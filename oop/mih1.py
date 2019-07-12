class A:
    def m1(self):
        print("Method m1() in A")


class B(A):
    def m2(self):
        print("Method m2() in B")


class C(A):
    def m1(self):
        print("Method m1() in C")


class D(B, C):
    pass


obj = D()
obj.m1()
print(D.mro())
