x = int(input())

coi = [500, 100, 50, 10, 5, 1]
ans = 0
for i in coi:
    y = x//i
    if i == 500:
        ans += 1000 * y
    elif i == 5:
        ans += 5 * y
print(ans)
