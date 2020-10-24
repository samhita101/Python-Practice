print("How long do you want your list to be?")
list_length = int(input())
first_list = []
sort_ed_list = []
for i in range(list_length):
    print("Enter Number:")
    num = float(input())
    first_list.append(num)

sorted_list = sorted(first_list)
temp_var = sorted_list[0]
sort_ed_list.append(temp_var)
for k in range(list_length):
    if temp_var != sorted_list[k]:
        sort_ed_list.append(sorted_list[k])

print(sort_ed_list)