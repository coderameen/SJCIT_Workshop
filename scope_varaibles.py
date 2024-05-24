
myn = 1000#global variable
class Student:
    #instance variable
    n1 = 10
    
    def display(self):
        n2 = 20#local varaible
        print(n2)
        print(self.n1)
        print(myn)
obj = Student()
obj.display()


        
    