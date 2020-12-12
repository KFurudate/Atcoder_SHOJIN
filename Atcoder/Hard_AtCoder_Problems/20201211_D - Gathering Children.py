import math

S = input()

n = len(S)
ans = [0] * n
for ri in range(2):

    cnt = 0
    for i in range(n):
        if S[i] == "R":
            cnt += 1
        else:
            ans[i] += math.floor(cnt / 2)
            ans[i - 1] += math.ceil(cnt / 2)
            cnt = 0

    ans = ans[::-1]
    S = S[::-1]
    S = S.replace('R', 'r').replace('L', 'R').replace('r', 'L')

print(*ans)