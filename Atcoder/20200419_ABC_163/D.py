#解説
def f_sum(l, r):
    return (l+r)*(r-l+1)//2

#n, k = map(int, input().split())
n, k = 3, 2
mod = 10**9 + 7

ans = 0
for i in range(k, n+2):
    l = f_sum(0, i-1)
    r = f_sum(n-i+1, n)
    ans += r-l+1

print(ans%mod)

