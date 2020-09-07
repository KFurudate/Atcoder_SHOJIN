from heapq import *

n, q = map(int, input().split())
A = []
B = []

Max = [[] * n+1] * n+1
Eql = []

def getMAX(i):
    if len(Max[i]) == 0: return -1
    return heappop(Max[i]) * (-1)


def addYochien(i):
    x = getMAX(i)
    if x == -1: return
    heappush(Eql, x)


def delYochien(i):
    x = getMAX(i)
    if x == -1: return
    Eql.remove(x)


def addEnji(i, x):
    delYochien(i)
    Max[i].append(-x)
    addYochien(i)


def delEnji(i, x):
    delYochien(i)
    if -x in Max[i]: Max[i].remove(-x)
    addYochien(i)


for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    addEnji(b, a)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    delEnji(B[c], A[c])
    B[c] = d
    addEnji(B[c], A[c])
    ans = heappop(Eql)
    print(Eql)
