n = int(input())

cnt = 0
while n:
    cnt = n%10
    n //= 10
print(cnt)