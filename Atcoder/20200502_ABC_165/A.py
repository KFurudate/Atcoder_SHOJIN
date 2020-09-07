k = int(input())
a, b = map(int, input().split())
n = b//k + 1

for i in range(n+1):
    if a <= (i*k) and (i*k) <= b:
        print('OK')
        exit()
print('NG')