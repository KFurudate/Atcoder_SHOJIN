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

################################
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


# N = ((2S+L-1)*L)/2
# 2N = (2S+L-1)*L

cnt = 0
n2 = 2 * n
for l in divisor(n2):
    s2 = (n2 / l) - l + 1
    if abs(s2) % 2 == 0:
        cnt += 1
print(cnt)