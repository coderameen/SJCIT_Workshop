#encapsulation: wrapping or binding the data in single entity/class
#bank managemens system, cyber security, Financial sectores....
class Student:
    n= 10#public
    _n= 20#protected
    __n =1000 #private
    def display(self):
        print(self.__n)
        print("dispay")
        
obj = Student()
print(obj.n)
print(obj._n)
# print(obj.__n)
obj.display()