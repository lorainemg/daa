from pprint import pprint

def gen_subsets(intervals):
    subsets = []
    for i in range(0, 2**len(intervals)):
        aux=[]
        for j in range(0, i):
            if (2**j & i) == 2**j:
                aux.append(intervals[j])
        subsets.append(aux)
    return subsets

def exhausted_search(h,elements):
    intervals = []
    for i in range(len(elements)) :
        for j in range(i,len(elements)) :
            intervals.append((i,j))

    subsets = gen_subsets(intervals)

    a=[]
    result = 0

    for i in range(len(subsets)):
        temp = list(elements)
        for x in subsets[i]:
            for j in range(x[0],x[1]+1):
                temp[j]= temp[j] + 1
        if len(temp)!= 0:
           b = all(i == h for i in temp)
           if b:
                a.append(subsets[i])
                result = result + 1

    return result

def solve(h, elems):
    return exhausted_search(h, elems)

#elems = [3, 7, 6]
h = 2
elems = [1, 1, 1]
result =exhausted_search(h,elems)
pprint(result)
