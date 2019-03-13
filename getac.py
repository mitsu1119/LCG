import sys

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
    M = int(sys.argv[1])

    x = []
    buf = input("number1 > ")
    x.append(int(buf))
    buf = input("number2 > ")
    x.append(int(buf))
    buf = input("number3 > ")
    x.append(int(buf))

    print(x)
    if x[0] == x[1]:
        a = 0
        c = x[0]
    else:
        a = (x[2] - x[1]) * modinv(x[1] - x[0], M) % M
        c = (x[2] - a * x[1]) % M

    print("a = {}".format(a))
    print("c = {}".format(c))
