class Myclass:
    def values(self,val1,val2):  #val1,val2 is local variable
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2

    def add(self):
        print(self.val1+self.val2)

mc=Myclass()
mc.values(10,20)
mc.add()
