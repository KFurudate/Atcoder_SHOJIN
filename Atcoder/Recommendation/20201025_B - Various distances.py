n = int(input())
X = list(map(int, input().split()))
m=0
y=0
t=0
for x in X:
    x = abs(x)
    m += x
    y += x**2
    t = max(t, x)
print(m)
print(y**0.5)
print(t)