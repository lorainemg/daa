import argparse
from pprint import pprint

def d(l, val, n):
    return min(abs(l-val), n - abs(l-val))

def recursive(a, i, j, val, n):
    if i == j:
        return d(a[i], val, n)
    
    _min = 2**32
    for k in range(i, j):
        for l in range(n):
            bst_a = recursive(a, i, k, l, n)
            bst_b = recursive(a, k + 1, j, l, n) 
            _min = min(_min,  bst_a + bst_b + d(l, val, n))
        
    return _min

def solve(n, m, cod, init):
    D = [(cod[i] - init[i]) % n for i in range(m)]
    return recursive(D, 0, len(D) - 1, 0, n)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='test file name')
    parser.add_argument('sol_file', help='solution file path')
    parser.add_argument('cant', help='number of tests')

    args = parser.parse_args()

    input_file = args.file
    out_file = args.sol_file
    cant = int(args.cant)

    f = open(input_file)
    sol = open(out_file)

    n, m = 0, 0
    c, init = None, None

    ok = 0
    bad = []

    for _ in range(cant):
        n = int(f.readline())
        m = int(f.readline())
        c = [int(c) for c in f.readline().split()]
        init = [int(c) for c in f.readline().split()]
        
        csol = int(sol.readline())
        if csol == solve(n, m, c, init):
            ok += 1
        else:
            bad.append((n,m,c,init))

        f.readline()
        sol.readline()

    print(ok)
    pprint(bad)

if __name__ == "__main__":
    #main()

    n = 10
    m = 3
    c = [2, 4, 10]
    init = [2, 6, 7]

    print(solve(n,m,c,init))