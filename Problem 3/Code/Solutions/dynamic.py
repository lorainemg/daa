from numpy import array
from pprint import pprint

def d(l, val, n):
    return min(abs(l-val), n - abs(l-val))

def dynamic(a, n):
    m = len(a)
    dp = [[[0 for _ in range(n) ] for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            for k in range(n):
                dp[i][j][k] = 2**32

    for i in range(m):
        for j in range(n):
            dp[i][i][j] = d(a[i], j, n)

    for size in range(1, m):
        for i in range(0, m - size):
            for v in range(n):
                j = i + size
                for k in range(i, j):
                    for l in range(n):
                 #       pprint(dp)
                        dp[i][j][v] = min(dp[i][j][v], dp[i][k][l] + dp[k+1][j][l] + d(l,v,n)) 
    
    return dp[0][m - 1][0]

def solve(n, m, cod, init):
    a = [(cod[i] - init[i]) % n for i in range(m)]
    return dynamic(a, n)


print(solve(10, 5, [2, 4, 10, 4, 5], [2, 6, 7, 2, 8]))