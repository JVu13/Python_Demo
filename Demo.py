def remove_chars(phrase, num):
    p = phrase[num:]
    return p

        


phrase = input("Type a phrase: ")
num = int(input("enter niumber: "))


print("Original String is", phrase)

print(remove_chars(phrase, num))

