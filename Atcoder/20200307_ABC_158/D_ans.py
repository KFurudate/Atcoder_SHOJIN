#データ構造
s = input()
q = int(input())
Q = [list(map(str, input().split())) for _ in range(q)]

t = ''
for qi in Q:
    if int(qi[0]) == 1:
        s, t = t, s
    else:
        if int(qi[1]) == 1:
            t += qi[2]
        else:
            s += qi[2]

t = t[::-1]
t += s
print(t)
