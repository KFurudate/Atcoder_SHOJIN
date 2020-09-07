N = 20
S = 'xxzaffeeeeddfkkkkllq'

#N = int(input())
#S = input()



"""
checklist = []

for i in range(N-1):
    j = i+1
    if S[i] != S[j]:
        checklist.append(S[i])
print(len(checklist)+1)
"""

#########
count = 1
for i in range(N-1):
    j = i+1
    if S[i] != S[j]:
        count += 1
print(count)