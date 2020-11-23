n = int(input())
n = 2025-n

def divisor(n):
    lower, upper = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n//i)
        i += 1
    return lower + upper[::-1]

for i in divisor(n):
    if i > 9: continue
    j = n//i
    if j > 9: continue
    print(f"{i} x {j}")