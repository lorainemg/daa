from random import randint 

def input_gen(n, m, tests = 100):
    file = open('test_problem3', 'w')
    for i in range(tests):
        t = gen(n, m)
        cod = gen(n, m)
        file.write(f"{n}\n") #n
        file.write(f"{m}\n") #n
        file.write(" ".join([str(i) for i in cod]) + "\n")
        file.write(" ".join([str(i) for i in t]) + "\n\n")        


def gen(n, m): 
    c = [0] * m
    for i in range(m):
        c[i] = randint(1, n)
    return c

input_gen(10, 5,tests=100)