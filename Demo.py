phrase = input("Type a phrase: ")
i = 0

print("Original String is", phrase)
print("Printing only even index chars ")

while i < len(phrase):
    if i % 2 == 0:
        print(phrase[i])
    i = i + 1