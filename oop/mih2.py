class A:
    def m1(self):
        print("Method m1() in A")


class B(A):
    def m1(self):
        print("Method m1() in B")


class C(B,A):
    pass


print(C.mro())
