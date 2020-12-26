# prompts user
print("User give me a number:")
users_limit = int(input())
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if users_limit < 1:
    print("give an integer between 1 - 26 please")
if users_limit > 26:
    print("give a number less than 27")
# prints desired output
for j in range(1, users_limit+1):
    for i in range(j):
        print(alphabet[j], end="") # end is so that all alphabets that are same stay on one line
    print("\r")


