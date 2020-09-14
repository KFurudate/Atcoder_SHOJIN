import math

n = int(input())
MOD = 10**9+7
print(10^0)

if n == 1:
    print(0)

elif n == 2:
    print(2)

else:
    ans = 2 * math.factorial(n)*10^(n-2)
    ans %= MOD
    print(ans)