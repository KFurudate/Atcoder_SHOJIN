import math

r, d = map(int, input().split())

area = (r*r)*math.pi
circumference = 2*d*math.pi
print(area*circumference)
