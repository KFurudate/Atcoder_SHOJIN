n = int(input())

Record = [0] * 6
for _ in range(n):
    a, b = map(float, input().split())
    if a >= 35:
        Record[0] += 1

    if 30 <= a and a < 35:
        Record[1] += 1

    if 25 <= a and a < 30:
        Record[2] += 1

    if 25 <= b:
        Record[3] += 1

    if 0 <= a and b < 0:
        Record[4] += 1

    if 0 > a:
        Record[5] += 1

print(*Record)
