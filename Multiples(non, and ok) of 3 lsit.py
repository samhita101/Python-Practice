# prompting user/collecting input for limit/defining empty lists for appropriate values to be appended into
print("User, give me a number, and I will find the number of multiples of three.")
print("Give me a number:")
number = int(input())
num_list1 = []
num_list2 = []

# finding number of multiples of 3 until users limit/appending each value into num_list1
# finding number of non-multiples of 3 until users limit/appending each value into num_list2,but removing even #'s
for i in range(number+1):
    if i % 3 == 0:
        num_list1.append(i)
    else:
        num_list2.append(i)
        if i % 2 == 0:
            num_list2.remove(i)

# printing list1
print(num_list1, "is the list of multiples of 3")

# printing num_list2
print(num_list2, "is the list of non - multiples of 3")
