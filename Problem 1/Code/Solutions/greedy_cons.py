from improve_permutation import get_cost
from pprint import pprint
import argparse

def greedy_cons(n, start, c, d):
  
    def greedy(n, start, c, d):
        result = [start]
        c[start] = 0
        while n > 1:
            max = c[0]
            start = 0
            for i in range(len(c)):
                if max < c[i]:
                    max = c[i]
                    start = i
            c[start] = 0
            result.append(start)
            n = n - 1
        return tuple(result)

    t = greedy(n, start, list(c), list(d))
    return t, get_cost(t, c, d)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='tests filename')
    parser.add_argument('dest', help='solution file destiny')
    parser.add_argument('cant', help='number of tests in file')

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

        t, b = greedy_cons(n, start, c, d)
        out.write(f"{start}\n{d}\n{c}\n")
        out.write(f"{t} -> {b}\n\n")

if __name__ == "__main__":
    main()