list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = []

for i in list1:
    for j in list2:
        new_list.append(i + j)

print (new_list)