import fractions

a, b = map(int, (input().split()))
#lcm = least common multiple

print(a*b//fractions.gcd(a, b))