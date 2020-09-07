n = int(input())
V = sorted(list(map(int, input().split())))

tmp = V[0]
for v in V[1:]:
    tmp = (tmp + v)/2

print(tmp)