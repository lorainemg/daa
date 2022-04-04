from random import randint 
import argparse

def input_gen(tests = 100, filename = 'test_problem4'):
    file = open(filename, 'w')
    for i in range(tests):
        n = randint(2, 10)
        t = gen(n)
        file.write(" ".join([str(i) for i in t]) + "\n\n")

def gen(n = 4, maxN = 20): 
    a = [0] * n
    a[0] = randint(1, maxN)
    for i in range(1, n):
        a[i] = a[i - 1] + (randint(1,maxN))
    return a

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='the test file name')
    parser.add_argument('tests', help='number of tests')

    args = parser.parse_args()

    filename = args.filename
    tests = int(args.tests)

    input_gen(tests, filename)