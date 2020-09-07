S = input()

if S[0] != "A":
    print("WA")
    exit()
if S[2:-1].count("C") != 1:
    print("WA")
    exit()

cnt = 0
for s in S:
    if s.isupper():
        cnt += 1
if cnt == 2:
    print("AC")
else:
    print("WA")



