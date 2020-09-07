from collections import defaultdict

n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = [int(input()) for _ in range(m)]

ans_dic = defaultdict(int)
for b in B:
    for i in range(n):
        if b >= A[i]:
            ans_dic[i+1] += 1
            break

print(max(ans_dic, key=ans_dic.get))