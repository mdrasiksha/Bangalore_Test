 class myclass:
    __a=10
    def display(self):
        print(self.__a)

obj = myclass()
obj.display()

print(myclass.__a) #no access because private method

