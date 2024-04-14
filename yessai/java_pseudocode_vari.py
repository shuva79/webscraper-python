import itertools

file = open("java_stuff.txt", "r")
listt = []

for file_line in file:
    listt.append(file_line.split(','))
    # for file_line_ in file_line.split('\n'):
    #     print(file_line_.split(","))

list_objects = []

for list_1 in listt:
    list_1 = list_1[0].split(" ")
    list_objects.append(list_1[1])
list_objects_ = list(set(list_objects))

file_2 = open("java_stuff_.txt", "w")

for list_1 in listt:
     list_1_ = list_1[0].split(" ")
     for aa in list_objects_:
         if aa == list_1_[1]:
            list_1[len(list_1) - 1] = list_1[len(list_1) - 1].replace(";\n", ' : ')
            print(f"- {list_1_[2]}", end="")
            [print(f",{list_1[x]}", end="") for x in range(1, len(list_1))]       
            print(f"{list_1_[1]}")
               

