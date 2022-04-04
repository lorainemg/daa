from random import randint
import argparse

def input_gen(tests = 100, filename = 'test_problem2'):
    file = open(filename, 'w')
    for i in range(tests):
        h = randint(2, 15)
        n = randint(2, 10)
        t = gen(n, h)
        file.write(str(h) + "\n")
        file.write(" ".join([str(i) for i in t]) + "\n\n")

def gen(n, h):
    d = [0] * n
    for i in range(0, n):
        d[i] = randint(1, h)
    return d

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='the test file name')
    parser.add_argument('tests', help='number of tests')

    args = parser.parse_args()

    filename = args.filename
    tests = int(args.tests)

    input_gen(tests, filename)