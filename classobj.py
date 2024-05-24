#class: it is a blue print by which object follows
#object: instance of classs
class StudentDetails:
    n = 10#instance variable
    def myfunc(self):
        print("This is local function")
        
obj = StudentDetails()
obj.myfunc()
print(obj.n)



class Student:
    def myfunc(self,name,usn):
        print(f"The Studen name is: {name} | usn is {usn}")
        
s1 = Student()
s1.myfunc('Alen',"CSO1")