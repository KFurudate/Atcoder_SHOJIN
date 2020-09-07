c1, c2, c3 = map(int, input().split())
c4, c5, c6 = map(int, input().split())
c7, c8, c9 = map(int, input().split())

if c1-c4 == c2-c5 == c3-c6 and \
   c1-c7 == c2-c8 == c3-c9 and \
   c4-c7 == c5-c8 == c6-c9:
    print('Yes')
else:
    print('No')