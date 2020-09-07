h, w, k = map(int, input().split())
C = [list(map(str, input())) for _ in range(h)]

n = h + w
tmp = [0] * (n)
for idx, ch in enumerate(C):
    tmp[idx] = ch.count("#")
    for i, c in enumerate(ch):
        if c == "#": tmp[i + 2] += 1

# print(tmp)

if k > w:
    cnt = 1
    for i in range(n):
        if tmp[i] == k: cnt += 1

else:
    cnt = 0
    for i in range(n):
        if tmp[i] == k: cnt += 1
        for j in range(n - i):
            if i == j: continue
            if (tmp[i] + tmp[j]) == k: cnt += 1
print(cnt)