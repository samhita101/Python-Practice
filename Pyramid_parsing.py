print("User give me a word:")
word = str(input())

for i in range(len(word)):
    print(word[:i+1:1])
