#n, k, c = map(int, input().split())
#s = input()
n, k, c = 11, 3, 2
s = 'ooxxxoxxxoo'

def getPositions():
    res = []
    i = 0
    while i < n:
        if s[i] == 'o':
            res.append(i)
            i += c + 1
        else:
            i += 1
    return res

l = getPositions()

s = s[::-1]
r = getPositions()
for i in range(k):
    r[i] = n-1-r[i]
s = s[::-1]

lastL = [-1]*(n+1)
for i in range(k):
    lastL[l[i]+1] = i

for i in range(n):
    if lastL[i+1] == -1:
        lastL[i+1] = lastL[i]

lastR = [-1] * (n+1)
for i in range(k):
    lastR[r[i]] = i
for i in range(n-1, -1, -1):
    if lastR[i] == -1:
        lastR[i] = lastR[i+1]

for i in range(n):
    if s[i] == 'x': continue
    li = lastL[i]
    ri = lastR[i+1]

    cnt = 0
    if li != -1: cnt += li+1
    if ri != -1: cnt += ri+1
    if (li != -1) and (ri != -1) and (r[ri]-l[li] <= c): cnt -= 1
    if cnt >= k: continue
    print(i+1)