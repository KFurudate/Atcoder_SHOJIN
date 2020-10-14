n = int(input())
SP = sorted([(list(map(str, input().split())), i+1) for i in range(n)])

def print_ans(lst):
    lst = sorted(lst, reverse=True)
    for l in lst:
        print(l[2])

sp, idx = SP[0]
s, p = sp[0], int(sp[1])
ans = [(p, s, idx)]

i = 1
while i < n:
    sp, idx = SP[i]
    s, p = sp[0], int(sp[1])
    if s == ans[0][1]:
        ans.append((p, s, idx))
    else:
        print_ans(ans)
        ans = [(p, s, idx)]
    i += 1

print_ans(ans)