# TLE
n = int(input())
MOD = 10**9 + 7

power = 1
for i in range(1, n+1):
    power *= i

print(power%MOD)

##################################
# 162 ms
from math import factorial

n = int(input())
MOD = 10**9 + 7

print(factorial(n)%MOD)

###############################
# 46 ms	
n = int(input())
MOD = 10**9 + 7

power = 1
for i in range(1, n+1):
    power *= i
    power %= MOD

print(power)