import collections

n = int(input())
A = list(map(int, input().split()))

x = []
x_append = x.append

for a in A:
    x_append(a - 1)
    x_append(a)
    x_append(a + 1)

X = collections.Counter(x)

print(X.most_common()[0][1])