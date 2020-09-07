a, b, c, x, y = map(int, input().split())

ans = 0
if x >= y:
    if (a+b) >= 2*c:
        ans = min(2*c*y + a*(x-y), 2*c*x)
    else:
        ans = a*x+b*y

else:
    if (a+b) >= 2*c:
        ans = min(2*c*x + b*(y-x), 2*c*y)
    else:
        ans = a*x+b*y

print(ans)

#################################
a, b, c, x, y = map(int, input().split())
ans = 0

def Cal(A, B, C, D, E):
    if (A+B) >= 2*C:
        ans = min(2*C*E + A*(D-E), 2*C*D)
    else:
        ans = A*D+B*E
    return ans

if x >= y:
    ans = Cal(a, b, c, x, y)
else:
    ans = Cal(b, a, c, y, x)

print(ans)