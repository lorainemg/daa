from improve_permutation import get_cost
from pprint import pprint
import argparse

def greedy_acum(n, start, c, d):
  
    def greedy(n, start, c, d):
        result = [start]
        c[start] = 0
        while n > 1:
            data = get_data(start, c ,d)
            old_start = start
            max = data[0]
            start = 0
            for i in range(len(c)):
                if max < data[i]:
                    max = data[i]
                    start = i
            rg = list(range(old_start + 1, start) if old_start < start else range(old_start - 1, start, - 1))
            for i in rg:
                if i not in result:
                    c[i] = 0
                    result.append(i)
                    start = i
                    break
            else:
                result.append(start)
                c[start] = 0
            n = n - 1
        return tuple(result)

    t = greedy(n, start, list(c), list(d))
    return t, get_cost(t, c, d)


def get_data(start, c, d):
    acum = [0] * len(c)
    for i in range(start + 1, len(c)):
        acum[i] = acum[i - 1] + c[i] / abs(d[start] - d[i])
    for i in range(start - 1, -1, -1):
        acum[i] = acum[i + 1] + c[i] / abs(d[start] - d[i])
    #print(acum)
    return acum

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

        t, b = greedy_acum(n, start, c, d)
        out.write(f"{start}\n{d}\n{c}\n")
        out.write(f"{t} -> {b}\n\n")

if __name__ == "__main__":
    main()