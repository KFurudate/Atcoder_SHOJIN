#https://abc005.contest.atcoder.jp/tasks/abc005_4
#https://upura.hatenablog.com/entry/2019/04/01/212701
import numpy as np

n = int(input())
dd = np.zeros((n+1, n+1), dtype=np.int64)
dd[1:, 1:] = np.array([input().split() for _ in range(n)], dtype=np.int64)

#二次元累積和
Sd = dd.cumsum(axis=0) #sum over rows for each column
SS = Sd.cumsum(axis=1) #sum over columns for each row

#面積の総和の最大値
Max_val = np.zeros(n*n+1, dtype=np.int64)
for x in range(1, n+1):
    for y in range(1, n+1):
        area = x * y
        val = SS[x:, y:] - SS[x:, :-y] - SS[:-x, y:] + SS[:-x, :-y]
        Max_val[area] = max(Max_val[area], val.max())
np.maximum.accumulate(Max_val, out=Max_val)

q = int(input())
P = [int(input()) for _ in range(q)]

for p in P:
    print(Max_val[p])