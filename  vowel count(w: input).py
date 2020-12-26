print("give me a string.")
string = str(input())
counter = 0

vlist = ["a", "e", "i", "o", "u"]

for x in range(len(string)):
    if string[x] in vlist:
        counter = counter + 1
    else:
        continue

print(counter, "is the number of vowels in your string.")