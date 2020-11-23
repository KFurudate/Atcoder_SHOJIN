n = int(input())

h = n//3600
n -= h*3600
m = n//60
n -= m*60

h = str(h)
m = str(m)
n = str(n)

if len(h) == 1: h = "0" + h
if len(m) == 1: m = "0" + m
if len(n) == 1: n = "0" + n

print(f"{h}:{m}:{n}")