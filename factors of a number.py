print("Give me a number.")
number = int(input())
factor_list = []

for i in range(1, number):
    if number % i == 0:
        factor_list.append(i)
    else:
        continue

factor_list.append(number)

print(factor_list)