import sys
K, P, N = map(int, sys.stdin.readline().split())

def cal(n, p):
    if n == 1:
        return p
    ans = cal(n // 2, p)
    if n % 2:
        return ans * ans * p % 1000000007
    else:
        return ans * ans % 1000000007


print(K * cal(N * 10, P) % 1000000007)