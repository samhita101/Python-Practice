# prompting user/collecting input for limit/defining empty list for values to be appended into
print("User, give me a number, and I will find the number of multiples of three.")
print("Give me a number:")
number = int(input())
num_list = []

# finding the number of 3's until users limit, and appending each value into the empty list

for i in range(0,number+1):
    if i % 3 == 0:
        num_list.append(i)
    else:
        continue


# removing 0 from the list, and printing list
num_list.remove(0)
print(num_list)


