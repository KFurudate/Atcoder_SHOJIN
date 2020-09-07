#周期
#n, k = 6, 727202214173249351
#A = [6, 5, 2, 5, 3, 2]

n, k = map(int, input().split())
A = list(map(int, input().split()))

Town = []
#まだ訪れていない町は-1
rec = [-1] * (n+1)
idx = 1
#周期までループをまわす
while (rec[idx] == -1):
    rec[idx] = len(Town)
    Town.append(idx)
    idx = A[idx-1]

#周期前
Exce = rec[idx]
#周期内
Cycl = len(Town) - Exce

if Exce > k:
    print(Town[k])
else:
    Warp = (k - Exce) % Cycl
    print(Town[Exce+Warp])