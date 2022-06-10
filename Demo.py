temp = 0
total = 0

first_n = int(input("Input a range: "))

for i in range(first_n):
    if i > 1:
        temp = i - 1
    total = i + temp
    print("Current Number ", i , "Previous Number ", temp, "Sum: ", total)
