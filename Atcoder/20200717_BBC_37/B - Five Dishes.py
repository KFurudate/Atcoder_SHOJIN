from itertools import permutations

Order = [int(input()) for _ in range(5)]

ans = []
for orders in permutations(Order):
    # print(orders)
    tmp = 0
    cnt = 1
    for order in orders:
        tmp += order
        if cnt == 5:
            ans.append(tmp)
        for _ in range(11):
            if tmp % 10 == 0:
                break
            tmp += 1
        cnt += 1

print(min(ans))