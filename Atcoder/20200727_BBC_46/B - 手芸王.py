import copy

n = int(input())
S = input()

ans = "b"
idx = 0
while len(ans) < len(S):

    ans = "a" + ans + "c"
    idx += 1
    if len(ans) >= len(S):
        break

    ans = "c" + ans + "a"
    idx += 1
    if len(ans) >= len(S):
        break

    ans = "b" + ans + "b"
    idx += 1
    if len(ans) >= len(S):
        break

if ans == S:
    print(idx)
else:
    print(-1)
