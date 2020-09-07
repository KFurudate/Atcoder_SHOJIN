N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        try:
            w = (N * h * n) / (4 * (h * n) - (N * n) - (N * h))
        except:
            continue
        if w.is_integer() and w > 0:
            if 4 * (h * n * w) == N * ((n * w) + (h * w) + (h * n)):
                ans = [h, n, int(w)]
                exit(print(' '.join(map(str, ans))))