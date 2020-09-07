import collections

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

S = collections.Counter(s)
T = collections.Counter(t)

ans = [0]
for key, cont in S.most_common():
    if cont > T[key]:
        ans.append(cont - T[key])
print(max(ans))

#Counterにはmost_common()メソッドがあり、(要素, 出現回数)という形のタプルを出現回数順に並べたリストを返す。