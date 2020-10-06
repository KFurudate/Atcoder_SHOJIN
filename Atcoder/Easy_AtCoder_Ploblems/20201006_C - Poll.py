# TLE
from collections import Counter

n = int(input())
S = [input() for _ in range(n)]
C = Counter(S)

ans = []
for key, val in C.most_common():
    if val == C.most_common()[0][1]:
        ans.append(key)
    else:
        break
for a in sorted(ans):
    print(a)
######################################
# TLE
n = int(input())
S = [input() for _ in range(n)]
set_S = sorted(list(set(S)))
ans = [0]*len(set_S)

for s in S:
     ans[set_S.index(s)] += 1
max_ans = max(ans)
for i in range(len(ans)):
    if ans[i] == max_ans:
        print(set_S[i])
##################################
from collections import Counter

n = int(input())
S = [input() for _ in range(n)]
C = Counter(S)
C_most = C.most_common()

ans = []
for key, val in C_most:
    if val == C_most[0][1]:
        ans.append(key)
    else:
        break

print(*sorted(ans), sep='\n')