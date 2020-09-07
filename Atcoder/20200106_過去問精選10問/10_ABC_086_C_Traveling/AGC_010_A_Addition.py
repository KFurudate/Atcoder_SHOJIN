n = int(input())
A = list(map(int, input().split()))
o = [a for a in A if a % 2 != 0]

if len(o) % 2 != 0:
    print('NO')
else:
    print('YES')