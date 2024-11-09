from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        pass
class B(A):
    def display(self):
        print("this is display method")
obj=B()
obj.display()





