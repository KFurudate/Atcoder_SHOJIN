from collections import Counter

n = int(input())

tmp = list("indeednow")
tmp_c = Counter(tmp)
tmp_c_val, tmp_c_cnt = zip(*tmp_c.most_common())
set_c_val = set(tmp_c_val)
#print(tmp_c['w'])
#print(set_c_val)


S = [input() for _ in range(n)]

for s in S:
    tmp_s = Counter(list(s))
    s_val, s_cnt = zip(*tmp_s.most_common())
    if len(set(s_val) & set_c_val) != len(set_c_val):
        print("NO")
    else:
        for key in set_c_val:
            #print(key)
            if tmp_c[key] != tmp_s[key]:
                print("NO")
                break
        else:
            print("YES")