from partition import solve as part
from imp_partition import solve as imp_part
from dynamic_partition import solve as dynamic

from pprint import pprint
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Tests file')
    parser.add_argument('cant', help='Number of Tests')

    args = parser.parse_args()

    input_file = args.file
    cant = int(args.cant)

    f = open(input_file)

    st = None

    ok = 0
    bad = []

    for _ in range(cant):
        st = [int(e) for e in (f.readline().split())]
        f.readline()

        d = dynamic(st)
        ip = imp_part(st)

        if d[0] == ip[0]:
            ok += 1
        else:
            bad.append((d, ip))
    
    print(ok)
    pprint(bad)
    
if __name__ == "__main__":
    main()