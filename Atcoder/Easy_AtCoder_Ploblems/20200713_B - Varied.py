S = input()

S_list = [s for s in S]
if len(S) == len(set(S_list)):
    print("yes")
else:
    print("no")