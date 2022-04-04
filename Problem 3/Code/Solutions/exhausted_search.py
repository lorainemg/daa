def exhausted_search(cod, init, n):
    c = 0
    while True:
        if transform(cod, init, n, c):
            return c
        c += 1

def check(cod, init): 
    return all([t[0] == t[1] for t in zip(cod, init)])

def transform(cod, init, n, c):
    if c == 0:
        return check(cod, init)

    for i in range(len(init)):
        for j in range(1, len(init) - i + 1):
            mov_right(init, i, j, n)
            r = transform(cod, init, n, c - 1) 
            mov_left(init, i, j, n)

            mov_left(init, i, j, n)
            l = transform(cod, init, n, c - 1)
            mov_right(init, i, j, n)
            
            if r or l:
                return True
                
    return False

def mov_right(init, idx, l, n):
    for i in range(idx, idx + l):
        init[i] = (init[i] + 1) % n
    
def mov_left(init, idx, l, n):
    for i in range(idx, idx + l):
        init[i] = (init[i] - 1) % n
    
def solve(n, m, cod, init):
    return exhausted_search(cod, init, n)

n = 10
m = 3
c = [2, 4, 10]
init = [2, 6, 7]

print(solve(n,m,c,init))