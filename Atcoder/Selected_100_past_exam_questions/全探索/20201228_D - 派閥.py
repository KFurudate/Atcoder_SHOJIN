n, m = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(m)]

ans = 1
for bit in range(2 ** n):
    pattern = []
    for i in range(n):
        if (bit >> i) & 1:
            pattern.append(i)
            print(bit)

    flg = True
    for idx, xx in pattern:
        for i in range(idx+1, len(pattern)):
            yy = pattern[i]
            if (xx, yy) not in XY:
                flg = False
                break
    if flg and ans < len(pattern):
        ans = len(pattern)

print(ans)
