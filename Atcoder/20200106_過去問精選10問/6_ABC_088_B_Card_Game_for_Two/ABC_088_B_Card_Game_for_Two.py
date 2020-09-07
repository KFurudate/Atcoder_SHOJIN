n = int(input())
a = list(map(int, input().split()))

Alice = []
Bob = []
for i in range(n):
    if i % 2 == 0:
        Alice.append(max(a))
    else:
        Bob.append(max(a))
    a.remove(max(a))

print(sum(Alice)-sum(Bob))


