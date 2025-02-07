def getprime(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:

        if prime[p]:

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = [p for p in range(2, n + 1) if prime[p]]
    return primes


n = int(input())
prime = getprime(n)
count = 0
for i in range(6, n + 1):
    temp = 0
    for p in prime:
        if i % p == 0:
            temp += 1
        if temp == 2:
            break
    if temp == 2:
        count += 1
print(count)








