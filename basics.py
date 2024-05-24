print("Hello all this is python!!")

name = "Alen"
#To check the type of data(datatype)
print(type(name))#<class 'str'>

n = 10
print(type(n))

n = 5.314#float
print(type(n))#<class 'float'>


name = "Alen"
age = 36
print(name)
print("The name is: ",name, " and the age is: ",age)
print(f"The name is {name} | age is {age}")
print("The name is {1} and age is {0}".format(age,name))




#to take input from user
# n1 = int(input("Enter first number"))
# n2 = int(input("Enter second number"))
# print(n1 + n2)
# print(type(n1))#<class 'str'>
# print(type(n2))#<class 'str'>
# print("The sum of numbers is: ",n1+n2)#The sum of numbers is:  50

#conditional statement
# n = int(input("Enter the number"))#3,10
# if n >=5:
#     n = n+100
# print(n)


#even or odd
# n = int(input("Enter number to check even or odd"))
n = 4
if n%2 == 0:
    print("Even number")
else:
    print("odd ")
    
a = 10
b = 30
c = 20
if a>b and a>c:
    print(a, " is greater")
elif b>a and b>c:
    print(b," is greater")
else:
    print(c, " is greater")
    
#iterative/looping statement
#1-10
for i in range(1,11):
    print(i, end=" ")
    
print()



#print only even numbers from 1 to 10
for i in range(1,11):
    if i%2!=0:
        print(i)
        
#whileprint
i = 1
while i<=10:
    print(i, end=" ")
    i = i+1
    #i+=1
    
print() 

#unconditional statement
#q: write a program to print 1 to 10 if 5 encounters terminate
for i in range(1,11):
    if i==5:
        break
    print(i)
print("---------------------")
#q: write progra
# m to print 1 to 10 except 5
for i in range(1,11):
    if i == 5:
        continue
    print(i)
    
#python Datastructures
#list 
l = [10,20,30,40]
#type
print(type(l))#<class 'list'>
#access: indexing
# print(l[4])

l = [10,20,30,40,50]
print(l[1:4])
print(l[1:])
print(l[-1])

#adding items/elements
l = [10,20,30]
l.append(100)
print(l)#[10, 20, 30, 100]

l.insert(0,5)#[5, 10, 20, 30, 100]
print(l)
l.insert(2,15)
print(l)#[5, 10, 15, 20, 30, 100]

l = [10,20]
l.extend([33,44,55])
print(l)


#remove element
l = [10,20,30,40]
#pop(): it remove last element
# l.pop(0)
l.remove(30)
print(l)


d = {"name":"Alen","age":30}
# print(len(d))
#add the element in dictionary
d['address'] = "Bangalore"
print(d)#{'name': 'Alen', 'age': 30, 'address': 'Bangalore'}

d2 = {"usn":"CS01"}
d.update(d2)


print("------------------")
d = {'name': 'Alen', 'age': 30, 'address': 'Bangalore', 'usn': 'CS01'}
print(d['name'])
# print(d['marks'])

print(d.get('name'))
print(d.get('address'))
print(d.get('marks',0))

#To Remove element from dictionary
d = {'name': 'Alen', 'age': 30, 'address': 'Bangalore', 'usn': 'CS01'}

del d['usn']
print(d)#{'name': 'Alen', 'age': 30, 'address': 'Bangalore'}