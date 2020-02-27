import math
n = 1000

isprime = list()
for i in range(n + 1):
    isprime.append(True)
isprime[0] = isprime[1] = False

# エラトステネスのふるい
k = 2
while (k < n):
    # 素数の2倍から順に消していく
    if isprime[k]:
        i = k * 2
        while i < n:
            isprime[i] = False
            i += k
    k += 1

# 素数のみ表示
prime = list()
for i in range(n+1):
    if isprime[i]:
        prime.append(i)
print(prime)