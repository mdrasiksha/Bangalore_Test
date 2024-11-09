class myclass:
    def __display(self):
        print("this is display1 method")

    def display2(self):
        print("this is display2 method")
        self.__display()

obj=myclass()
obj.__display()
