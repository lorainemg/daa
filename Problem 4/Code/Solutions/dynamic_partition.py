from pprint import pprint
import numpy as np

def dynamic(elems):
    n = len(elems)
    dp = [[0] * (n) for _ in range(n)]
    dp_max = [[0] * (n) for _ in range(n)]
    back = []

    for j in range(n):
        for i in range(n):
            if i + j >= n:
                continue
            k = 0
            m = j - 1
            minP = dp_max[k][m] + (i+1)*(dp[k][m]/(k+1) + elems[i+j])
            pair = (k,m)
            while m > 0:
                k += 1
                m -= 1
                if minP > dp_max[k][m] + (i+1)*(dp[k][m]/(k+1) + elems[i+j]):
                    minP = dp_max[k][m] + (i+1)*(dp[k][m]/(k+1) + elems[i+j])
                    pair = (k, m)
            if len(back) == j + 1:
                back[-1] = pair
            if len(back) < j + 1:
                back.append(pair)
            t = back[-1]
            dp[i][j] = (i+1)*(dp[t[0]][t[1]]/(t[0]+1) + elems[i+j])
            dp_max[i][j] = dp_max[t[0]][t[1]] + dp[i][j]
    return dp_max,back

def solve(elems):
    part = []
    cost = 1 << 16
    dp_max, l = dynamic(elems)
    k = 0
    m = len(elems) - 1
    minP = dp_max[k][m]
    pair = (k,m)            
    while m > 0:
        k += 1
        m -= 1
        if minP > dp_max[k][m]:
            minP = dp_max[k][m]
            pair = (k, m)

    p = [elems[pair[1]:pair[0]+pair[1]+1]]
    c = dp_max[pair[0]][pair[1]]
    row = l[pair[1]][0]
    col = l[pair[1]][1]  
    p.extend([elems[col:row+col+1]])
    nxt = l[col]
    while nxt[1] >= 0:
        row = nxt[0]
        col = nxt[1]
        p.append(elems[col:row+col + 1])
        nxt = l[col]
    if cost >= c:
        part = p
        cost = c

    part.reverse()
    return cost, tuple([tuple(p) for p in part])