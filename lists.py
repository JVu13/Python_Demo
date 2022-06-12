list1 = ["mike", "","Emma","Kelly","","brad"]

for i in list1:
    if i == "":
        list1.remove(i)

print(list1)