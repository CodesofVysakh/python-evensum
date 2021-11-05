list_objects = [1,2,3,4,5,6]
x = []

for i in list_objects:
    if i%2 != 0:
        x.append(i)

list_objects = x
print(list_objects)