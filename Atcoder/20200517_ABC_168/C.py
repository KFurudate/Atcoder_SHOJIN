import math

a, b, h, m = map(int, input().split())
P = math.pi

#Hour hand
xh = a * math.sin(h*P/6 + m*P/360)
yh = -a * math.cos(h*P/6 + m*P/360)

#Minute hand
xm = b * math.sin(m*P/30)
ym = -b * math.cos(m*P/30)

print(((xh-xm)**2+(yh-ym)**2)**0.5)
