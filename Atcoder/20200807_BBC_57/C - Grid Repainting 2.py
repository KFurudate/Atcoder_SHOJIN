h, w = map(int, input().split())
S = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        #print(S[i][j])
        cnt = 0
        if i == 0 or i == h - 1:
            cnt += 1
        if j == 0 or j == w - 1:
            cnt += 1

        if S[i][j] == "#" and i+1 < h and S[i+1][j] != "#":
                cnt += 1

        if S[i][j] == "#" and j+1 < w and S[i][j+1] != "#":
                cnt += 1

        if S[i][j] == "#" and i-1 > 0 and S[i-1][j] != "#":
                cnt += 1

        if S[i][j] == "#" and j-1 > 0 and S[i][j-1] != "#":
                cnt += 1

        if cnt == 4:
            print("No")
            exit()
print("Yes")