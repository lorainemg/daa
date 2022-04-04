from pprint import pprint
import argparse

def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:] 
        yield [ [ first ] ] + smaller

def solution(st):
    partitions = list(partition(st))
    res = []
    for part in partitions:
        res.append(tuple(sorted([tuple(p) for p in part], key=lambda t: max(t))))
    return [tuple(r) for r in res]

def get_cost(perm):
    acc_sum = 0
    res = 0
    for subst in perm:
        acc_sum += max(subst)
        res += acc_sum * len(subst)
    return res

def calculate_cost(permutations):
    best = None
    res = None
    for perm in permutations:
        if best is None:
            best = get_cost(perm)
            res = perm
            continue
        partial = get_cost(perm)
        if partial < best:
            best = partial
            res = perm
    return best, tuple(res)

def solve(st):
    return calculate_cost(solution(st))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='tests filename')
    parser.add_argument('dest', help='solution file destiny')
    parser.add_argument('cant', help='number of tests')

    args = parser.parse_args()

    input_file = args.file
    out_file = args.dest
    cant = int(args.cant)

    f = open(input_file)
    out = open(out_file, mode='w')

    st = None

    for _ in range(cant):
        st = [int(e) for e in (f.readline().split())]
        f.readline()

        b, t = solve(st)
        out.write(f"{t} -> {b}\n\n")
    
if __name__ == "__main__":
    #main()
    st = [8, 9, 27, 38, 54, 74, 80, 87]
    pprint(solve(st))