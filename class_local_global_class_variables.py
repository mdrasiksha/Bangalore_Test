i,j = 15,25   #global variable
class MyClass:
    a,b=10,20   #class variable
    def add(self,x,y):  #local variable
        print(x+y)
        print(i+j)

p1=MyClass()
p1.add(5,2)