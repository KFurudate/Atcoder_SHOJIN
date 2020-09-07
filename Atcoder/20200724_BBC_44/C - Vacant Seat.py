import math
n = int(input())

print(0)
s = input()
if s == "Vacant": exit()
Even = s
if Even == "Male":
    Odd = "Female"
else:
    Odd = "Male"

# print(Even, Odd)

Seat = [i for i in range(n)]
Predict_Seat = [Even if s % 2 == 0 else Odd for s in Seat]
tmp = (n + 1) // 2

while True:
    if Seat[tmp] == -1: continue
    else:
        print(Seat[tmp])
        s = input()
        if s == "Vacant": exit()

        if Predict_Seat[tmp] == s:
            tmp += math.ceil(tmp / 2)
        else:
            tmp -= math.ceil(tmp / 2)

        Seat[tmp] = -1
    # print(tmp)
    # print(Seat)

