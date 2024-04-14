file = open("java_stuff.txt", "r")
listt = []

for file_line in file:
    listt.append(file_line.split(' '))
    # for file_line_ in file_line.split('\n'):
    #     print(file_line_.split(","))


list_objects = []

for list_1 in listt:
    list_1 = list_1[1].split(".")
    list_objects.append(list_1)

print(list_objects)
file_2 = open("java_stuff_.txt", "w")

for list_1 in list_objects:
        list_1[len(list_1) - 1] = list_1[len(list_1) - 1].replace(";\n", '')
        
        if (list_1[0] == "javax"):
            print(f"IMPORT {list_1[len(list_1) - 1]} class from the {list_1[0]}.{list_1[1]} package")
        elif (list_1[0] == "java"):
            print(f"IMPORT {list_1[len(list_1) - 1]} class from the {list_1[0]}.{list_1[1]}.{list_1[2]} package")
            

