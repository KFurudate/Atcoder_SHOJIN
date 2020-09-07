n, k = map(int, input().split())
D = list(map(int, input().split()))

N = str(n).split()

like_n = set(N) ^ set(diff)


diff = [1, 2, 3, 4, 5, 6, 7, 8, 9]


like_n = sorted(list(set(D) ^ set(diff)))

if [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] == like_n:
    print(n)
elif like_n[0] == 0:
    print(like_n[0] * n)
else:
    print(like_n[1] * n)
###################
n, k = map(int, input().split())
D = list(map(int, input().split()))

for i in range(10001):
    if i >= n and