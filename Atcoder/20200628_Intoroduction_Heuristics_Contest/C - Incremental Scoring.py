#Thanks for https://atcoder.jp/contests/intro-heuristics/submissions/14809214

D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
T = [int(input())-1 for _ in range(D)]

def calc_score(T):
    last = [0] * 26
    score = 0
    for d in range(D):
        v = T[d]
        score += S[d][v]
        for i in range(26):
            if i == v:
                last[i] = 0
            else:
                last[i] += 1
            score -= C[i] * last[i]
        # print(score)
    return score

m = int(input())
for _ in range(m):
    d, q = map(int, input().split())
    d -= 1
    q -= 1
    old = T[d]
    T[d] = q
    new_score = calc_score(T)
    print(new_score)

################################
#Thanks for https://atcoder.jp/contests/intro-heuristics/submissions/14809214

import sys
input=lambda :sys.stdin.readline().rstrip()

D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
T = [int(input())-1 for _ in range(D)]

def calc_score(T):
    last = [0] * 26
    score = 0
    for d in range(D):
        v = T[d]
        score += S[d][v]
        for i in range(26):
            if i == v:
                last[i] = 0
            else:
                last[i] += 1
            score -= C[i] * last[i]
        # print(score)
    return score

m = int(input())
DQ = [list(map(int, input().split())) for _ in range(m)]
for d, q in DQ:
    d -= 1
    q -= 1
    old = T[d]
    T[d] = q
    new_score = calc_score(T)
    print(new_score)

###################

import sys
input=lambda :sys.stdin.readline().rstrip()

D = int(input())
*C, = map(int, input().split())
S = [tuple(map(int, input().split())) for _ in range(D)]
T = [int(input())-1 for _ in range(D)]

def calc_score(T):
    last = [0] * 26
    score = 0
    for d in range(D):
        v = T[d]
        score += S[d][v]
        for i in range(26):
            if i == v:
                last[i] = 0
            else:
                last[i] += 1
            score -= C[i] * last[i]
        # print(score)
    return score

m = int(input())
DQ = [list(map(int, input().split())) for _ in range(m)]
for d, q in DQ:
    d -= 1
    q -= 1
    T[d] = q
    new_score = calc_score(T)
    print(new_score)