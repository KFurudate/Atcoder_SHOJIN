S = input()

ans = ""
for s in S:
    if s == "0":
        ans += "0"
    if s == "1":
        ans += "1"
    if s == "B":
        ans = ans[:-1]

print(ans)
