import sys
from functools import reduce
import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No modinv")
    return x % m

if __name__ == "__main__":

    # inputs
    x = []
    buf = input("number1 > ")
    x.append(int(buf))
    buf = input("number2 > ")
    x.append(int(buf))
    buf = input("number3 > ")
    x.append(int(buf))
    buf = input("number4 > ")
    x.append(int(buf))
    buf = input("number5 > ")
    x.append(int(buf))
    buf = input("number6 > ")
    x.append(int(buf))

    # solve M
    T = []
    for x0, x1 in zip(x, x[1:]):
        T.append(x1 - x0)

    zeros = []
    for t0, t1, t2 in zip(T, T[1:], T[2:]):
        zeros.append(t2 * t0 - t1 * t1)

    M = abs(reduce(math.gcd, zeros))

    # solve a, c
    if x[0] == x[1]:
        a = 0
        c = x[0]
    else:
        a = (x[2] - x[1]) * modinv(x[1] - x[0], M) % M
        c = (x[2] - a * x[1]) % M


    # answer
    print("a = {}".format(a))
    print("c = {}".format(c))
    print("M = {}".format(M))
