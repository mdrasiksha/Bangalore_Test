class Myclass:
    name="kumar"
    def __init__(self,name):
        print(name)  #constructor argument local
        print(self.name) #represent class variable

c=Myclass("pavan")