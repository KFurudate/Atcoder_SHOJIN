from itertools import permutations

n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
patterns = tuple(permutations(list(range(n))))
dist = []

for per in patterns:
    pre_x, pre_y = XY[per[0]]
    for idx in per[1:]:
        x, y = XY[idx]
        tmp = ((pre_x-x)**2+(pre_y-y)**2)**0.5
        dist.append(tmp)
        pre_x, pre_y = x, y

print(sum(dist)/len(patterns))