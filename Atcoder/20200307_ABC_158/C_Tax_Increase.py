a, b = map(int, input().split())
x = max(a * 12.5, b * 10)
if round(x * 0.08, 0) == a and round(x * 0.1, 0) == b:
    print(int(x))

else:
    print(-1)
###################
import math

a, b = map(int, input().split())
for i in range(1251):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(int(i))
        exit()
print(-1)
##################
import math
a, b = map(int, input().split())
for i in range(1251):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(int(i))
        exit()
print(-1)




