from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("eat Non veg")

class Cow(Animal):
    def eat(self):
        print("eat veg")

t=Tiger()
t.eat()

c=Cow()
c.eat()
