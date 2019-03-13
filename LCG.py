import sys
import time

def LCG(seed, a, c, M, size):
    res = []
    x = seed

    for i in range(size):
        x = (a * x + c) % M
        res.append(x)

    return res

if __name__ == "__main__":
    a = int(sys.argv[1])
    c = int(sys.argv[2])
    M = int(sys.argv[3])
    size = int(sys.argv[4])

    res = LCG(time.time_ns(), a, c, M, size)

    print(res)
