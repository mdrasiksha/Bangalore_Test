class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("this is m2 method from class B")

object1=A()
object1.m1()

object2=B()
object2.m2()

