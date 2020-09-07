import sys
input=lambda :sys.stdin.readline().rstrip()
n = int(input())
S = [input() for _ in range(n)]

S_unique = list(set(S))
print(len(S_unique))
