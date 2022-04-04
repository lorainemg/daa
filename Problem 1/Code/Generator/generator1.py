from random import randint 
import argparse

def input_gen(tests = 100, filename = 'test_problem1'):
    file = open(filename, 'w')
    for _ in range(tests):
        n = randint(2, 8)
        t = gen(n)
        file.write(f"{n}\n") #n
        file.write(" ".join([str(i) for i in t[0]]) + "\n")
        file.write(" ".join([str(i) for i in t[1]]) + "\n")
        file.write(str(t[2]) + "\n\n")

def gen(n = 4): 
    d = [0] * n
    c = [0] * n
    c[0] = randint(1,20)
    pos = randint(0, n - 1)
    for i in range(1, n):
        d[i] = d[i - 1] + (randint(1,20))
        c[i] = randint(1,20)
    return d, c, pos

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='the test file name')
    parser.add_argument('tests', help='number of tests')

    args = parser.parse_args()

    filename = args.filename
    tests = int(args.tests)

    input_gen(tests, filename)