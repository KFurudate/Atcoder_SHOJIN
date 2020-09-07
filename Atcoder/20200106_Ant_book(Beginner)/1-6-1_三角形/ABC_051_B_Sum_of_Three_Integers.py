k, s = map(int, input().split())


cont = 0
for x in range(k+1):
    for y in range(k+1):
        if x + y <= s:
            if s - (x+y) <= k:
                cont += 1
print(cont)