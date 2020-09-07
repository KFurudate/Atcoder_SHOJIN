N = 4
K = 150
h = [150, 140, 100, 200]

#import sys
#sys.setrecursionlimit(1000000000)
#N, K = input().strip().split()
#h = list(map(int, input().split()))
count = 0
for i in range(N):
    if h[i] >= K:
        count += 1
print(count)

#count = 0
#for i in h:
#    if i >= K:
#        count += 1

#N, K = input().split()
#h = list(map(int, input().split()))
#count = [i for i in h if i >= K]
#print(len(count))
