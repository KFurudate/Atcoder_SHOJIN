n = int(input())
W = [input() for _ in range(n)]

if len(W) > len(set(W)):
    exit(print("No"))

tmp = W[0][-1]
for w in W[1:]:
    if w[0] != tmp:
        exit(print("No"))
    tmp = w[-1]

print("Yes")
