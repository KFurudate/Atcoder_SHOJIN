S = int(input())

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

cnt = 0
for i in divisor(S):
    a1 = (S/i)+(i-1)/2
    if a1.is_integer():
      cnt += 1
print(cnt)