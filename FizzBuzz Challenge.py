print("Give me a number.")
num = int(input())

if num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 15 == 0:
    print("FizzBuzz")
else:
    print(num)