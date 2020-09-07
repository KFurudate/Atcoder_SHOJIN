n, a, b = map(int, input().split())

from scipy.special import comb
ans = comb(n, r, exact=True)
print(ans)