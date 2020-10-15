S = list(input())

string = ""
tmp = ""
cnt = 0
for s in S:
    string += s
    if string != tmp:
        cnt += 1
        string, tmp = "", string
print(cnt)