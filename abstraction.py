#Abstraction: Hiding the implementation detail by showing essential detiails
#example: installatioin of any softwares
from abc import ABC, abstractmethod
class absClass(ABC):
    @abstractmethod
    def myabsfunc(self):
        pass
class ConcreteClass(absClass):
    def myabsfunc(self):
        print("This is my abstract method")
        
obj = ConcreteClass()
obj.myabsfunc() 