n, m, l = map(int, input().split())
P, R, Q = map(int, input().split())

if P > n or P > m or P > l or \
   R > n or R > m or R > l or \
   Q > n or Q > m or Q > l:
   print(0)
   exit()

Cardboard = n*m*l
Package = P*R*Q

ans = Cardboard//Package
print(ans)

############################
n, m, l = map(int, input().split())
P, R, Q = map(int, input().split())

if P > n or P > m or P > l and \
   R > n or R > m or R > l and \
   Q > n or Q > m or Q > l:
   print(0)
   exit()

Package1 = n//P + m//R + l//Q
Package2 = n//P + m//Q + l//R
Package3 = n//R + m//P + l//Q
Package4 = n//R + m//Q + l//P
Package5 = n//Q + m//P + l//R
Package6 = n//Q + m//R + l//P

#ardboard = n*m*l

ans = (Package1, Package2, Package3, Package4, Package5, Package6)
#print(ans)
print(max(ans))
######################