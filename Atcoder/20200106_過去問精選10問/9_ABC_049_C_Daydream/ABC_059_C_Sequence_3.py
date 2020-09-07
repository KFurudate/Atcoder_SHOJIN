def main():
    import sys
    input = sys.stdin.readline

    #n = int(input())
    #A = list(map(int, input().split()))
    n=6
    A=[-1,4,3,2,-5,4]

    def Chk(a, pos):
        cnt = 0
        tmp = 0

        for a in A:
            tmp += a

            if pos and tmp < 1:
                cnt += 1 - tmp
                tmp = 1
            elif not pos and tmp > -1:
                cnt += 1 + tmp
                tmp = -1

            pos = not pos
        return cnt

    print(min(Chk(A, True), Chk(A, False)))

if __name__ == '__main__':
    main()