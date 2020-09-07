def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    A = []
    A_append = A.append
    cnt = 0

    for i in range(n-1):
        A_append(a[i])
        x = sum(A)
        if x > 0 and x + a[i+1] > 0:
            y = -(x + a[i+1] + 1)
            cnt -= y
            a[i+1] += y

        elif x < 0 and x + a[i+1] < 0:
            y = -(x - a[i+1] + 1)
            cnt += y
            a[i+1] += y

    if sum(a) == 0:
        cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()