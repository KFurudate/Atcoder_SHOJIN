# https://kakedashi-engineer.appspot.com/2020/04/12/abc023d/
# 割られた時の風船の高度は全て X 以下」を満たすような X の最小値を二分探索で求める

n = int(input())
HS = [list(map(int, input().split())) for _ in range(n)]

def is_ok(x):
    lst = [(x-HS[i][0])//HS[i][1] for i in range(n)]
    lst = sorted(lst)

    for j in range(n):
        if lst[j] < j:
            return False

    return True

def meguru_bisec(ng, ok):
    while (abs(ok - ng)> 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisec(0, int(1e+14)))

