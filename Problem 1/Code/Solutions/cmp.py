from permutation import solve as perm_sol
from improve_permutation import solve as imp_sol
from greedy_cons import greedy_cons
from greedy_avg import greedy as greedy_avg
from greedy_acum import greedy_acum
from recursive import solve as recursive

from time import time
from pprint import pprint
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Tests')
    parser.add_argument('cant', help='Number of Tests')

    args = parser.parse_args()

    input_file = args.file
    cant = int(args.cant)

    f = open(input_file)

    n,start = 0, 0
    d, c = None, None

    ok = 0
    bad = []

    for i in range(cant):
        n = int(f.readline())
        d = [int(dist) for dist in (f.readline()).split()]
        c = [int(cost) for cost in (f.readline()).split()]
        start = int(f.readline())
        f.readline()
        
        try: #testing solution
            r = recursive(n, start, c, d)
        except:
            print("EXECUTION ERROR")
            pprint(d)
            pprint(c)
            break

        ip = imp_sol(n, start, c, d) # correct solution
        if r == ip[1]:
            ok += 1
        else:
            bad.append((i, r, ip[1], r - ip[1], start == 0 or start == len(d)))

    print(ok)
    pprint(bad)
    
if __name__ == "__main__":
    main()