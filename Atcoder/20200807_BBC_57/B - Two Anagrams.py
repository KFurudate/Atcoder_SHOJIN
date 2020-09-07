S = input()
T = input()

sorted_S = sorted(S)
sorted_T = sorted(T, reverse=True)
if sorted_S < sorted_T:
    print("Yes")
else:
    print("No")
