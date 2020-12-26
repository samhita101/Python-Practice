# prompts user
print("User give me a number:")
users_limit = int(input())

# prints desired output
for j in range(users_limit,0,-1):
    for i in range(j,0,-1):
        print(10**(i-1),",", end="") # end is so that each line stops on the line, and so there are no new spaces
    print("\r")


