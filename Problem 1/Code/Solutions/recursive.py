from pprint import pprint
import argparse

def solve(n, start, c, d):

    def _solve(a, pos, acc, t):
        conspos = a[pos][0]
        distpos = a[pos][1]

        if len(a) == 1:
            acc = acc + a[0][0] * t
            return acc

        if pos == 0:
            a.remove(a[pos])
            return _solve(a, pos , acc + conspos * t, t + abs(distpos - a[pos ][1]))

        if pos == len(a) - 1:
            a.remove(a[pos])
            return _solve(a, pos - 1, acc + conspos * t, t+abs(distpos - a[pos - 1][1]))

        else:
            copya = list(a)
            
            a.remove(a[pos])
            x = _solve(a, pos - 1, acc + conspos*t, t + abs(distpos - a[pos - 1][1]))

            copya.remove(copya[pos])
            y = _solve(copya, pos, acc + conspos*t, t+abs(distpos - copya[pos][1]))

        return y if x > y else x

    copyto = list(zip(c,d))
    initpos = start

    cc  = _solve(copyto,initpos,0,0)
    return cc

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

        b = solve(n, start, c, d)
        out.write(f"{start}\n{d}\n{c}\n")
        out.write(f"Missing -> {b}\n\n")

if __name__ == "__main__":
    main()
