#RE
a, b = map(int, input().split())

if a <= 0 and b >= 0:
    print("Zero")

elif a < 0 and b < 0:
    if len(list(range(a, b+1))) % 2:
        print("Negative")
    else:
        print("Positive")

else:
    print("Positive")


##########################

a, b = map(int, input().split())

if a <= 0 and b >= 0:
    print("Zero")

elif a < 0 and b < 0:
    if (abs(a)-abs(b+1))%2:
        print("Negative")
    else:
        print("Positive")

else:
    print("Positive")