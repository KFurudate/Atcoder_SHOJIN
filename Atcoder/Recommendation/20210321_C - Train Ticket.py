abcd = input()

patterns = []
n = 3
# 要素の二択の全パターン(2**n)
for i in range(2 ** 3):
    pattern = []
    # 2進数表記でそれぞれの桁が0か1のどちらか判定
    for j in range(n):
    	# フラグが立っていた場合の処理
        if (i >> j) & 1:
            pattern.append(1)
        else:
            pattern.append(0)

    patterns.append(pattern)

a = abcd[0]
for pattern in patterns:
    memo = ""
    memo += a
    ans = int(a)
    for idx, p in enumerate(pattern, 1):
        if p == 0:
            ans -= int(abcd[idx])
            memo += "-"
            memo += abcd[idx]

        if p == 1:
            ans += int(abcd[idx])
            memo += "+"
            memo += abcd[idx]

    if ans == 7:
        memo += "="
        memo += "7"
        print(memo)
        exit()
