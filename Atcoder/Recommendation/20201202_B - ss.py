S = input()

for i in range(2, len(S), 2):
    S_ = S[:-i]
    half_point = len(S_) // 2
    first = S_[:half_point]
    second = S_[half_point:]
    if first == second:
        print(half_point*2)
        exit()