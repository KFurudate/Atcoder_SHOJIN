x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

ans = abs(x1-x2) + abs(y2-y1) + 1
print(ans)