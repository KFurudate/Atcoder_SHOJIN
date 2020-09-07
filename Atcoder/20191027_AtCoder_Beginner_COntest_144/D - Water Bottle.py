import math
#a, b, x = map(int, input().split())
a=3
b=1
x=8
s = x//a
rad = 0.0

if s >= a*b//2:
    h = (a*b-s)*2//a
    rad = math.atan2(h, a)
else:
    w = s*2//b
    rad = math.atan2(b, w)
PI = math.acos(-1)
deg = rad*360//(2*PI)
print(deg)
