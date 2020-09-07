abc = sorted(list(map(int, input().split())), reverse=True)
ans = 0

if abc[1]%2 != 0 and abc[2]%2 == 0:
    ans += 1
    abc[0] += 1
    abc[1] += 1

elif abc[1]%2 == 0 and abc[2]%2 != 0:
    ans += 1
    abc[0] += 1
    abc[2] += 1

ans += abc[0] - abc[1]
ans += (abc[1] - abc[2])//2

print(ans)




