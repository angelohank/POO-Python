class A():
    def myMethod(self):
        print('metodo da classe A')

    def myMethod2(self):
        print('segundo metodo da classe A')

class B(A):
    def myMethod(self):
        print('metodo da classe B')

class C(A):
    def myMethod(self):
        print('metodo da classe C')

class D(C, B):
    pass
    # def myMethod(self):
    #     print('metodo da classe D')


myClass = D()
myClass.myMethod()
myClass.myMethod2()