#メモ化再帰
import sys
sys.setrecursionlimit(10**5+10)

n = int(input())
h = [int(i) for i in input().split()]

#dpの最小値を変更する関数
def chmin(a, b):
    if a > b:
        return b
    else:
        return a

f_inf = float('inf')

#DPテーブルの初期化
dp = [f_inf] * (10**5+10)

#メモ化再帰の関数
def rec(i):
    #dpの値が更新されている場合はその値を返す
    if dp[i] < f_inf:
        return dp[i]
    #再帰の終了条件
    if i == 0:
        return 0
    res =f_inf
    res = chmin(res, rec(i-1)+abs(h[i]-h[i-1]))
    if i >1:
        res = chmin(res, rec(i-2) + abs(h[i]-h[i-2]))
    #結果をメモ
    dp[i]= res
    return res

ans = rec(n-1)
print(ans)
