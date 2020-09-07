import copy

num = int(input())
n = format(num, 'b')[::-1].find('1')

ans = copy.deepcopy(num)
for _ in range(n - 1):
    ans += num // 2
    num = num // 2

print(ans)