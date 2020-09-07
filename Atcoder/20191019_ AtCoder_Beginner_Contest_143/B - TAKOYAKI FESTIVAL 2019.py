#N = int(input())
#d_list = list(map(int, input().split()))

N=7
d_list=[5, 0, 7, 8, 3, 3, 2]
sum_num = 0
for i in range(N):
    for j in range(i+1, N):
        sum_num += d_list[i] * d_list[j]

print(sum_num)


