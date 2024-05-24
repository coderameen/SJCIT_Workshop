#Polymorphism: "Implementing same thing in a different way"
#we can achieve polymorhism using 1.overloading and 2.overriding

#1.Overloadding

#a. operator overloading
a = 10
b = 20
print(a+b)

a = "hello"
b = "python"
print(a+b)


l = [1,2,3]
print(l*2)#[1, 2, 3, 1, 2, 3] #Replication

print(2*30)

#method overloading
def add():
    print(10+20)
add()

def add(a,b):
    print(a+b)
add(40,50)

# def add(a,b,c):'
#     '
# add(10,20,30)


#Overriding
class Parent:
    def display(self):
        print("This is parent Property")

class Child(Parent):
    def display(self):
        super().display()
        print("This is child property")

c = Child()
c.display()
    
    
