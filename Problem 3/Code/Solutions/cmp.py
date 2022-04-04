from dynamic import solve as dynamic
from recursive import solve as recursive

from pprint import pprint
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Tests file')
    parser.add_argument('cant', help='Number of Tests')

    args = parser.parse_args()

    input_file = args.file
    cant = int(args.cant)

    f = open(input_file)

    n, m = 0,0
    cod, init = None, None

    ok = 0
    bad = []

    for _ in range(cant):
        n = int(f.readline())
        m = int(f.readline())
        cod = [int(c) for c in f.readline().split()]
        init = [int(c) for c in f.readline().split()]
        
        f.readline()

        d = dynamic(n, m, cod, init)
        r = recursive(n, m, cod, init)

        if d == r:
            ok += 1
        else:
            bad.append((d, r, ("DATA: ", n, m, cod, init)))
    
    print(ok)
    pprint(bad)
    
if __name__ == "__main__":
    main()