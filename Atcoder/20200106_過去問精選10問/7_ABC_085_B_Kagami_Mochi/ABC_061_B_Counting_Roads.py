n, m = map(int, input().split())

ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append(a)
    ab.append(b)

ans = [ab.count(i) for i in range(1, n + 1)]

for i in ans:
    print(i)