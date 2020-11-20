W = list(input())

ans = ""
lost = ["a", "i", "u", "e", "o"]

for w in W:
    if w in lost:
        continue
    ans += w
print(ans)