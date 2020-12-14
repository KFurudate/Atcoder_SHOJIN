from scipy.special import comb

L = int(input())
print(comb(L-1, 11, exact=True))