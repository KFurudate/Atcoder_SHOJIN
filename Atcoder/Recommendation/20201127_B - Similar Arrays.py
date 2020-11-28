n = int(input())
A = list(map(int, input().split()))

tmp = 1
for a in A:
    if a%2: continue
    tmp *= 2

print(3**n - tmp)

