n = int(input())

def divisor(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
        i += 1
    return lower + upper[::-1]


ans = 0
for i in range(1, n + 1):
    if i % 2:
        cnt = divisor(i)
        if len(cnt) == 8:
            ans += 1

print(ans)
