class Myclass:
    def m1(self):
        print("instance method")

    @staticmethod
    def m2(self):
        print("static method")

mc=Myclass()
mc.m1()
Myclass.m2(10)
