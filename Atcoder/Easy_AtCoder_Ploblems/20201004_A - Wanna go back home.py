S = list(set(input()))

if len(S) == 4:
    print("Yes")
elif len(S) == 2:
    if ("N" in S and "S" in S) or ("W" in S and "E" in S):
      print("Yes")
    else:
      print("No")
else:
    print("No")


