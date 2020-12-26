n = int(input())
print("Give me a number r that is LESS THAN the number n")
r = int(input())


def nCr(n, r):

    def factorial(p):
        fact = 1
        for i in range(1, p + 1):
            fact = fact*i
        return(fact)
    return((factorial(n)) / (factorial(r) * factorial(n-r)))

y = nCr(n, r)
print(y)
