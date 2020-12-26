# prompts user
print("User give me a number:")
users_limit = int(input())

# prints desired output
for j in range(1,users_limit+1):
    for i in range(j):
        print(j, "", end="") # end is so that each line stops on the line, and so there are no new spaces
    print("\r")


