#bit全探索
#解説AC

H, W, K = map(int, input().split())
C = [list(map(str, input())) for _ in range(H)]

ans = 0
#1<<n : 2^n
for i in range(1<<H):
    for j in range(1<<W):
      cnt = 0
      for h in range(H):
        for w in range(W):
          #1>>n : 下からn桁目(0 index)
          if (i>>h & 1): continue
          if (j>>w & 1): continue
          cnt += C[h][w] == '#'

      if cnt == K: ans += 1
print(ans)