def solve():
  import sys
  from collections import deque
  input = lambda: sys.stdin.readline().rstrip()
  n = int(input())
  A = list(map(int, input().split()))
  r, ans = 1, 1
  T = deque([])
  T_append = T.append
  T_popleft = T.popleft
  T_append(A[0])
  for l in range(n):
    while r < n:
      k = A[r]
      if k not in T:
        T_append(A[r])
        r += 1
      else:
        break
    ans = max(ans, len(T))
    if r == l: r += 1
    else: T_popleft()
  return ans

if __name__ == '__main__':
    print(solve())
##################

def solve():
  import sys
  from collections import deque
  input = lambda: sys.stdin.readline().rstrip()
  n = int(input())
  A = list(map(int, input().split()))
  l, r, ans =0, 1, 1
  T = deque([])
  T_append = T.append
  T_popleft = T.popleft
  T_append(A[0])
  while r < n:
    k = A[r]
    if k not in T:
        T_append(A[r])
        r += 1
        ans = max(ans, len(T))
    else:
        T_popleft()
        l += 1
  return print(ans)

if __name__ == '__main__':
    solve()
########################
#集合 重複する値がある場合は無視されて、一意な値のみが要素として残る。
def solve():
  import sys
  input = lambda: sys.stdin.readline().rstrip()
  n = int(input())
  A = list(map(int, input().split()))
  r, ans = 1, 1
  T = set()
  T.add(A[0])
  for l in range(n):
    while r < n and (A[r] not in T):
      T.add(A[r])
      r += 1
    ans = max(ans, len(T))
    if r == l: r += 1
    else: T.discard(A[l])
  return print(ans)

if __name__ == '__main__':
    solve()