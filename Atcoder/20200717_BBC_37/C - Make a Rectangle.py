n = int(input())
A = list(map(int, input().split()))

set_A = tuple(set(A))
Side_2 = []
Side_4 = []
for a in set_A:
    tmp = A.count(a)
    if (tmp >= 2) and (tmp < 4):
        Side_2.append(tmp)
    if tmp >= 4:
        Side_4.append(tmp)
        
if (len(Side_2) < 2) and not Side_4:
    print(0)
    exit()

if not Side_2 and Side_4:
    print(Side_4[-1] * 2)
    exit()

if (len(Side_2) >= 2) and not Side_4:
    print(Side_2[-1] * Side_2[-2])
    exit()

if (len(Side_2) == 1) and Side_4:
    max2 = Side_2[-1]
    max4 = Side_4[-1]
    if max4 >= max2:
        print(max4 * 2)
        exit()
    else:
        print(max4 * max2)
        exit()

if (len(Side_2) >= 2) and Side_4:
    max2 = Side_2[-1]
    max2_2 = Side_2[-2]
    max4 = Side_4[-1]
    if max4 >= max2:
        print(max4 * 2)
        exit()
    elif (max4 < max2) and (max4 <= max2_2):
        print(max2 * max2_2)
        exit()
    elif (max4 < max2) and (max4 > max2_2):
        print(max2 * max4)
        exit()


####################################
from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A_dic = Counter(A)

set_A = sorted((set(A)), reverse=True)
tmp = 0
for a in set_A:
    if A_dic[a] >= 4:
        print(max(tmp*a, a*a))
        exit()
    if A_dic[a] >= 2:
        ans = tmp * a
        if ans != 0:
            print(ans)
            exit()
        tmp = a
print(0)

#####################################








