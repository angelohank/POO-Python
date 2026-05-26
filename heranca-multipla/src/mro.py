class A():
    pass

class B(A):
    pass

class C(A):
    pass


class D(B, C):
    pass

print(C.__mro__)
print(D.__mro__)