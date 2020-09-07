N = 8
#A = [2, 3, 1]
keys=[8, 2, 7, 3, 4, 5, 6, 1]
N = int(input())
keys = list(map(int, input().split()))

values = [i for i in range(1, N+1)]
dic = dict(zip(keys, values))
keys.sort()
for i in range(1, N+1):
    value = dic[i]
    print('{} '.format(value), end='')





