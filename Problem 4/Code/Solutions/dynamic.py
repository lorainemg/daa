from pprint import pprint
import numpy as np

def dynamic(elems):
    n = len(elems)
    dp = [[0] * (n) for _ in range(n)]
    back = []

    for j in range(n):
        for i in range(n):
            if i + j >= n:
                continue
            k = 0
            m = j - 1
            if len(back) < j + 1:
                minP = dp[k][m]/(k+1) 
                pair = (k,m)
                while m > 0:
                    k += 1
                    m -= 1
                    if minP > dp[k][m]/(k+1):
                        minP = dp[k][m]/(k+1)
                        pair = (k, m)
            if len(back) == j + 1:
                t = back[-1]
                minP = dp[t[0]][t[1]]/(t[0]+1)
            elif len(back) < j + 1:
                back.append(pair)
            dp[i][j] = (i+1)*(minP + elems[i+j])
    return dp, back

def solve(elems):
    part = []
    cost = 1 << 16
    dp, l = dynamic(elems)
    print(np.array(dp))
    print(l)
    j = len(elems) - 1
    for i in range(len(l)):
        p = [elems[i:i+j+1]]
        c = dp[j][i]
        nxt = l[i]
        while nxt[1] >= 0:
            row = nxt[0]
            col = nxt[1]
            p.append(elems[col:row+col + 1])
            c += dp[row][col]
            nxt = l[col]
        if cost >= c:
            part = p
            cost = c
        j -= 1
    part.reverse()
    return cost, tuple([tuple(p) for p in part])