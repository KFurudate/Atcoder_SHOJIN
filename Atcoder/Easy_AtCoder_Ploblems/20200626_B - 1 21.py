a, b = map(str, input().split())
c = int(a + b)

for i in range(1, 1001):
    if c == i*i:
        print("Yes")
        exit()

print("No")

#####################

a, b = map(str, input().split())
c = int(a + b)

if (c ** .5).is_integer():
    print("Yes")
else:
    print("No")