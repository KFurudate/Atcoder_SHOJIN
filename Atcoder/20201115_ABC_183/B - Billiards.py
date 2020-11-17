Sx, Sy, Gx, Gy = map(int, input().split())

if Sx < Gx:
    ans = Sx + abs(Gx - Sx) * (Sy / (Sy + Gy))
else:
    ans = Gx + abs(Sx - Gx) * (Gy / (Sy + Gy))

print(ans)
