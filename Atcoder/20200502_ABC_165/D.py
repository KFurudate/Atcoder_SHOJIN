a, b, n = map(int, input().split())
x = n
if n >= b-1: x = b-1
ans = a*(x%b)//b
print(ans)