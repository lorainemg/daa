from pprint import pprint
import argparse

def get_permutation(n, start):

    def _perm(start, mark, sol, sol_set, idx):
        if idx == len(sol):
            sol_set.add(tuple(sol))
            return

        for i in range(len(sol)):
            if not mark[i]:
                sol[idx] = i
                mark[i] = True
                _perm(start, mark, sol, sol_set, idx + 1)
                mark[i] = False

    sol_set = set()
    mark = [False] * n
    sol = [0] * n
    mark[start] = True
    sol[0] = start
    _perm(start, mark, sol, sol_set, 1)
    return sol_set

def get_cost(perm, c, d):
    t = 0
    cons = 0
    cp = list(c)
    cp[perm[0]] = 0
    for i in range(1, len(perm)):
        t += abs(d[perm[i-1]] - d[perm[i]])
        cons += cp[perm[i]] * t
        cp[perm[i]] = 0
    return cons

def solution(sol_set, c, d):
    best = None
    tup = None
    for t in sol_set:
        if best is None:
            best = get_cost(t, c, d)
            tup = t
            continue
        b = get_cost(t, c, d)
        if b < best:
            best = b
            tup = t
    return tup, best

def solve(n, start, c, d):
    """ 
    n     -> number of lamps
    start -> start position
    c     -> lamps cost
    d     -> distance
    """
    return solution(get_permutation(n, start), c, d)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='tests file name')
    parser.add_argument('dest', help='Solution file destiny')
    parser.add_argument('cant', help='number of tests in the filename')

    args = parser.parse_args()

    input_file = args.file
    out_file = args.dest
    cant = int(args.cant)

    f = open(input_file)
    out = open(out_file, mode='w')

    n,start = 0, 0
    d, c = None, None

    for _ in range(cant):
        n = int(f.readline())
        d = [int(dist) for dist in (f.readline()).split()]
        c = [int(cost) for cost in (f.readline()).split()]
        start = int(f.readline())
        f.readline()

        t, b = solution(get_permutation(n, start), c, d)
        out.write(f"{start}\n{d}\n{c}\n")
        out.write(f"{t} -> {b}\n\n")

if __name__ == "__main__":
    main()