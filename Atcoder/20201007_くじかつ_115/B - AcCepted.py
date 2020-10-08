S = input()

if S[0] != "A":
    print("WA")
    exit()

if "C" not in S[2:-1]:
    print("WA")
    exit()

c_cnt = 0
for i in range(1, len(S)):
    if S[i] == "C":
        c_cnt += 1
    elif S[i].isupper():
        print("WA")
        exit()
    if c_cnt >= 2:
        print("WA")
        exit()

print("AC")
