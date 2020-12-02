n = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

if n > len(set(P)):
    print("NO")
    exit()
for i in (a, b):
    if i in P:
        print("NO")
        exit()

print("YES")
