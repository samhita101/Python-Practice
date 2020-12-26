# prompts user
print("User give me a number:")
users_limit = int(input())

# prints desired output
for j in range(users_limit, 0, -1):
    for i in range(j, 0, -1):
        print(j, ",", end="") # end is so that the each line stops on the same line and doesnt use another line as a space
    print("\r")



