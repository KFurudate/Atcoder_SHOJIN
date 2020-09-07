#偶奇 #組み合わせ
import math

n, m = map(int, input().split())

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if n <= 1 and m >=2:
    print(combinations_count(m, 2))
elif n >= 2 and m <=1:
    print(combinations_count(n, 2))
elif n <=1 and m <=1:
    print(0)
else:
    print(combinations_count(n, 2)+combinations_count(m, 2))

######
n, m = map(int, input().split())
ans = 0
ans += n*(n-1)//2
ans += m*(m-1)//2
print(ans)