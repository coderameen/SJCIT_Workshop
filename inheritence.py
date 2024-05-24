#Single level inheritence
class Parent:
    def pdisplay(self):
        print("This is parent property")
        
class Child(Parent):
    def cdisplay(self):
        print("This is child property")
        
obj = Child()
obj.cdisplay()
obj.pdisplay()


print("---------------------------------")




#multi level inheritence
class GrandParent:
    def gpdisplay(self):
        print("This is Grand parent property")
        
class Parent(GrandParent):
    def pdisplay(self):
        print("This is parent property")
        
class Child(Parent):
    def cdisplay(self):
        print("This is child property")

c1 = Child()
c1.cdisplay()
c1.pdisplay()
c1.gpdisplay()

print("-------------------------------")



#Muplitple inheritence
class Father:
    def fdisplay(self):
        print("This is father property")
        
class Mother:
    def mdisplay(self):
        print("This is mother property")
        
class Child(Father,Mother):
    def cdisplay(self):
        print("This is child property")
        
c = Child()
c.cdisplay()
c.fdisplay()
c.mdisplay()