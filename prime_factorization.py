print("I wants a number.")
x = int(input())
primes = []
prime_factors = []
final_factors = []


# function to find if number is prime or not
def prime_or_not(arg2):
    for i in range(2, arg2):
        if arg2 % i == 0:
            break
    else:
        return True


# finding all positive prime numbers less than x and appending to list primes
for k in range(2, x):
    if prime_or_not(k):
        primes.append(k)

# this is list of prime #'s less than x
print("Here is a list of primes numbers less than {}:".format(x), primes)


# finding prime factors that go into x
dividend = x
for m in range(len(primes)):
    while dividend % primes[m] == 0:
        prime_factors.append(primes[m])  # appending prime factor into primes_factors
        dividend = dividend//primes[m]  # defining dividend as new number that resulted from dividing by a prime factor

# printing list of prime factors of x
print("Here is the list of prime factors that go into {}:".format(x), prime_factors)

# code for returning list if x = prime
if len(prime_factors) == 0:
    prime_factors.append(1)
    prime_factors.append(x)
    print("Your number is prime.")
    print(prime_factors)

# making all factors into exponential form
temp_var = prime_factors[0]
m = 0
for g in range(len(prime_factors)):
    if prime_factors[g] == temp_var:
        m = m + 1
        print(prime_factors[g], "^", m)
    else:
        print(prime_factors[g])
        m = 0
        continue
