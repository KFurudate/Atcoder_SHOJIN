AB = [list(map(int, input().split())) for _ in range(3)]
# ans = [[1, 2], [2, 3], [3, 4]]
ans = [-1] * 3

for ab in AB:
    ab = sorted(ab)
    if ab == [1, 2]:
        ans[0] = 1
    if ab == [2, 3]:
        ans[1] = 1
    if ab == [3, 4]:
        ans[2] = 1

if ans == 3:
    print("YES")
else:
    print("NO")
##########################
AB = [list(map(int, input().split())) for _ in range(3)]

ans = [0] * 4
for a, b in AB:
    a -= 1
    b -= 1
    ans[a] += 1
    ans[b] += 1

if max(ans) >= 3:
    print("NO")
else:
    print("YES")






