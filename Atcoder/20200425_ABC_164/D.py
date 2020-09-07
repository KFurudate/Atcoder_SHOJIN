s = input()
if len(s) <= 4 and s != '2019':
    print(0)
    exit()

M_2019 = [2019 * i for i in range(1, 200001)]
S = [s[:i] for i in range(4, len(s))]
cnt = 0
for i_s in S:
    for j in range(len(i_s)-4):
        if int(i_s[j:]) in M_2019:
            cnt += 1

print(cnt)

##########
