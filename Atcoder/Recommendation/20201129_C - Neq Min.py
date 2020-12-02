#TLE
n = int(input())
P = list(map(int, input().split()))

ans = [i for i in range(n + 1)]

for p in P:
    if p in ans:
        ans.remove(p)
    print(ans[0])


#####################

n = int(input())
P = list(map(int, input().split()))

m = 0
ans = [0] * (n + 1)

for p in P:
    ans[p] = -1
    if m <= p:
        for i in range(m, len(ans)):
            if ans[i] != -1:
                m = i
                break

    print(m)

#############################
n = int(input())
P = list(map(int, input().split()))

m = 0
ans = [-1] * 200001

for p in P:
    ans[p] = 0
    if m == p:
        for i in range(m, len(ans)):
            if ans[i]:
                m = i
                break

    print(m)