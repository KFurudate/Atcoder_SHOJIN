N = 5
N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 != 0:
        count += 1

print(count/N)


#https://atcoder.jp/contests/abc142/tasks/abc142_a