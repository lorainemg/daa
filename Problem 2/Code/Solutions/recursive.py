from pprint import pprint

def solve(dif, pos, k, count):
    if pos == len(dif) - 1:
        if (dif[pos] == 0 or dif[pos] == 1) and k == 0:
            return 1
        if k == 1 and dif[pos] == 2:
            return 1
        if dif[pos] == k:
            return 1
        return 0

    tmp = 0
    if dif[pos] == k:
        tmp += solve(dif, pos + 1, k, count)
        n = dif[pos] + 1
        for j in range(1, n):
            tmp += j*k*solve(dif, pos + 1, k - j, count)
            #count += j*k*solve(dif, pos + 1, k , count)
        return tmp
    elif dif[pos] < k:
        return (k - dif[pos])*solve(dif, pos + 1, dif[pos], count)
    else:
        tmp += solve(dif, pos + 1, dif[pos], count)
        rg = range(1,2) if k == 0 else range(1, k+1)
        for i in rg:
            tmp += i*(k+1)*solve(dif, pos + 1, dif[pos] - i, count)
    return tmp


if __name__ == "__main__":
    seq = [1, 2, 3, 4]
    h = 5
    dif = [h - seq[i] for i in range(len(seq)) ]
    print(solve(dif, 0, dif[0], 0))
