class Myclass:
    def m1(self):
        pass
c1=Myclass()
c2=Myclass()
c3=c1
print(id(c1))
print(id(c2))
print(id(c3))
