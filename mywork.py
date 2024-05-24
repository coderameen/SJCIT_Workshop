l = [10,20,30,40]
l[1] = 2000
print(l)#[10, 2000, 30, 40]

# t = (10,20,30,40)
# t[1] = 200
# print(t)#TypeError: 'tuple' object does not support item assignment

s = {10,20,30}
d = {1:10,2:20,3:30}
d[2] = 200
print(d)#{1: 10, 2: 200, 3: 30}


# l = []
# d = {"name":"Alen","age":30}
# l.append(d)
# d2 = {"name":"bob","age":20}
# l.append(d2)
print("-------------------")
l = [{'name': 'Alen', 'age': 30}, {'name': 'bob', 'age': 20}]
for i in l:
    print(i['age'])
print("------------")