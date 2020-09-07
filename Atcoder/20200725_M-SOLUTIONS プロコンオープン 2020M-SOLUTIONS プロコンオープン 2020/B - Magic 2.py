#イコールが抜けていた（＞＜）
a, b, c = map(int, input().split())
k = int(input())

for _ in range(k):
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
    # print(a, b, c)

if (a < b) and (b < c):
    print("Yes")
else:
    print("No")
