print("Please enter an integer [no words, letters, or 0s]: ")
number = int(input())
for i in range(1,11):
    i = 1
while i < 11:
    print(number, "*", i, "=", number*i)
    i=i+1