import sys
input = sys.stdin.readline

x, y, a, b, c = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

d = []
d_append = d.append
for i in range(x):
    d_append(P[i])

for i in range(y):
    d_append(Q[i])

for i in range(c):
    d_append(R[i])

d.sort(reverse=True)

ans = 0
for i in range(x+y):
    ans += d[i]

print(ans)