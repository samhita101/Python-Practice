print("Number Monster is hungry.  Give number.")
num = int(input())

#  We convert number to string, then extract each character and re-convert to integer.
digit_list = [int(x) for x in str(num)]
print(digit_list)

for i in range(len(digit_list)):
    print(digit_list[i] * (10 ** (len(digit_list)-(i+1))))
