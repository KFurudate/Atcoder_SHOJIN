n = int(input())
A = list(map(int, input().split()))

Colors = []
High_scorer = []
for a in A:
    if a < 400:
        Colors.append("Gray")
    if 400 <= a and a < 800:
        Colors.append("Brown")
    if 800 <= a and a < 1200:
        Colors.append("Green")
    if 1200 <= a and a < 1600:
        Colors.append("Light_blue")
    if 1600 <= a and a < 2000:
        Colors.append("Blue")
    if 2000 <= a and a < 2400:
        Colors.append("Yellow")
    if 2400 <= a and a < 2800:
        Colors.append("Orange")
    if 2800 <= a and a < 3200:
        Colors.append("Red")
    if 3200 <= a:
        High_scorer.append(a)

MIN = len(set(Colors))
H = len(High_scorer)

if MIN >= 1:
    print(MIN, (MIN+H))
elif MIN == 0:
    print(1, H)



